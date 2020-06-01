from django import forms

#Automaticamente comprueba que todos los valores introducidos son validos
class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)