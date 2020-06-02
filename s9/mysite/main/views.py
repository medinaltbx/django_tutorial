from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

#id = igual a lo que pongamos despues de "/" en el buscador y lo muestra
def index(response, id):
	ls = ToDoList.objects.get(id=id)

	if response.method == "POST":
		print(response.POST)
		if response.POST.get("save"):
			for item in ls.item_set.all():
				if response.POST.get("c" + str(item.id)) == "clicked":
					item.complete = True
				else:
					item.complete = False

				item.save()


		elif response.POST.get("newItem"):
			txt = response.POST.get("new")
			
			if len(txt) > 2:
				ls.item_set.create(text=txt, complete=False)
			else:
				print("invalid")

	return render(response, "main/list.html", {"ls":ls})

def home(response):
	return render(response, "main/home.html", {})

#Crea un nuevo objeto ToDoList
def create(response):
	#Si intenamos hacer cambios o pasar informacion de la form a la pagina
	if response.method == "POST":
		#Contiene un diccionario que tiene todas las ids de todos los diferentes atributos de la form y guarda los valores que contienen
		form = CreateNewList(response.POST) 

		#Si los valores introducidos son validos
		if form.is_valid():
			#Accede a la variable nombre, la limpia y la usa para crear un nuevo objeto ToDoList.
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		#Redirecciona a la pagina que tiene la ToDoList que se crea. Esto es porque pasa el id como http. ...
		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()

	#Pasa la form creada al html
	return render(response, "main/create.html", {"form":form}) 