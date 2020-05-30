from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

#id = igual a lo que pongamos despues de "/" en el buscador y lo muestra
def index(response, id):
	ls = ToDoList.objects.get(id=id)
	return render(response, "main/list.html", {"ls":ls})

def home(response):
	return render(response, "main/home.html", {})