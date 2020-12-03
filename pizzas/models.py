from django.db import models

# Create your models here.
#create class models and define our fields?
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)

   
    #we dont need meta sub class because plural of topping is toppings
    def __str__(self):
        return f"{self.name[:50]}..."

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name[:50]}..."
