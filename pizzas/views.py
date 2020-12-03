from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import PizzaForm, ToppingForm, CommentForm

# Create your views here.
#user is reuqesting info so the first function is index(request)
#homepage
def index(request): 
    return render(request,'pizzas/index.html')

#get all pizzas function
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'pizzas':pizzas}

    return render(request,'pizzas/pizzas.html',context)

#get individual pizzas function and toppings ordered by date added(or most recent)
def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    comments =pizza.comment_set.order_by('-date_added')

    context = {'pizza':pizza,'toppings':toppings,'comments':comments}

    return render(request,'pizzas/pizza.html', context)


def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('pizzas:pizzas')
    context = {'form': form}

    return render(request,'pizzas/new_pizza.html',context)


def new_topping(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            #create new topping without saving it to the database
            new_topping = form.save(commit=False)
            #assign the pizza of the new topping based on the pizza we pulled from pizza_id
            new_topping.pizza = pizza
            new_topping.save()
            form.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form,'pizza':pizza}
    return render(request,'pizzas/new_topping.html',context)


def edit_topping(request,topping_id):
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza 

    if request.method !='POST':
        form = ToppingForm(instance=topping)
    else:
        form= ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza',pizza_id=pizza.id)

    context = {'topping':topping,'pizza':pizza,'form':form}
    return render(request,'pizzas/edit_topping.html',context)



def new_comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            #create new topping without saving it to the database
            new_comment = form.save(commit=False)
            #assign the pizza of the new topping based on the pizza we pulled from pizza_id
            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form,'pizza':pizza}
    return render(request,'pizzas/new_comment.html',context)

def edit_comment(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    pizza = comment.pizza 

    if request.method !='POST':
        form = CommentForm(instance=comment)
    else:
        form= CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza',pizza_id=pizza.id)

    context = {'comment':comment,'pizza':pizza,'form':form}
    return render(request,'pizzas/edit_comment.html',context)
#def comment(request,pizza_id):
    #pizza = Pizza.objects.get(id=pizza_id)

    #if request.method != 'POST':
        #form = PizzaForm()

