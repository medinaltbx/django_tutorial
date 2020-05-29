from django.db import models

# Create your models here.
class ToDoList(models.Model):
    #nombre del atributo     CharField tipo de atributo y cuanto ocupa
    name = models.CharField(max_length=200)

    #devuelve nombre
    def __str__(self):
        return self.name

#los items forman parte de ToDoList
class Item(models.Model):
    #on delete cascade quiere decir que cuando se elimine un objeto ToDoList se eliminan todos los Items asociados a el
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text