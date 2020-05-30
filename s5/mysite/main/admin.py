from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.
#Se ha de registrar aqui para que aparezca en la pagina de administracion
admin.site.register(Item)
admin.site.register(ToDoList)