from django.urls import path

from . import views 

urlpatterns = [
#Si no escribe nada despues de "/" -> envia a index
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
] 