from django.urls import path

from . import views 

urlpatterns = [
#Si no escribe nada despues de "/" -> envia a index
path("<str:name>", views.index, name="index"),

] 