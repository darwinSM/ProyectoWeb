from django import forms

class FormularioContacto (forms.Form):
    nombre = forms.CharField (label='Nombre' , max_length= 20 , required= True)
    email = forms.EmailField (label = 'Email' , required= True)
    contenido = forms.CharField(label= 'Contenido' , required=True , widget=forms.Textarea)