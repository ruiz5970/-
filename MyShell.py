import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","pizzeria.settings")

import django 
django.setup()

from pizzas.models import Pizza 

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print("Pizza ID:",pizza.id,"Pizza:", pizza)

#we have a string method in models (__str__(self)) which returns the text of the object PIZZA
#find where pizza id =1
p = Pizza.objects.get(id=1)
print(p.text)
print(p.date_added)

#SELECT ALL similar
toppings = p.topping_set.all()

for topping in toppings:
    print(topping)


#og base
#{% extends "pizzas/base.html" %}

#{% block content %}

#<p>Pizzas Home</p>

#<p>Pizzeria allows you to make your own pizza with the toppings you desire! </p>

#{% endblock content %}#



#og index
#{% extends "pizzas/base.html" %}

#{% block content %}

#<p>Pizzas Home</p>

#<p>Pizzeria allows you to make your own pizza with the toppings you desire! </p>

#{% endblock content %}

#og pizzas 
#{% extends "pizzas/base.html" %}

#{% block content %}
#<p>Pizzas </p>

#<ul>

   # {% for pizza in pizzas %}

    #    <li><a href="{% url 'pizzas:pizza' pizza.id %}">{{ pizza }}</a></li>
    #{% empty %}
        #<li> No pizzas have been added yet. </li>
    #{% endfor %}
#</ul> 

#<a href="{% url 'pizzas:new_pizza' %}">Add a new pizza</a>


#{% endblock content %}



#PIZZA OG
'''
{% extends "pizzas/base.html" %}

{% block content %}
<p>Pizza Toppings : {{ pizza.text }}</p>

<ul>

    {% for t in toppings %}

        <li>
            <p>{{ t.date_added|date:'M d, Y H:i' }}</p>

            <p>{{ t.name|linebreaks }} </p>
            <p>
                <a href="{% url 'pizzas:edit_topping' t.id %}">Edit Topping</a>
            </p>

        </li>
        {% empty %}
        <li> There are no toppings for this pizza yet.</li>
        {% endfor %}
        
        
</ul>

<p>Comments:</p>
<ul>
{% for c in comments %}

        <li>
            <p>{{ c.date_added|date:'M d, Y H:i' }}</p>

            <p>{{ c.name|linebreaks }} </p>
            <p>
            <a href="{% url 'pizzas:edit_comment' c.id %}">Edit Comment</a>
            </p>
        </li>
        {% empty %}
        <li> There are no comments for this pizza yet.</li>
   
    {% endfor %}



    </ul>













<p>
    <a href="{% url 'pizzas:new_topping' pizza.id %}">Add a new topping</a>
    <a href="{% url 'pizzas:new_comment' pizza.id %}">Add a new comment</a>
</p>



{% endblock content %} '''