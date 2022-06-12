from django import forms
from django.urls import path
from django.core.exceptions import ValidationError
from computerApp.models import Machine
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('machines/',
        views.machine_list_view,
        name='machines'),
    path('machine/<pk>',
        views.machine_detail_view,
        name='machine - detail'),
]

class createMachineForm(forms.Form):
    nom = forms.CharField(
        label="Nom de la machine"
    )
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 6:
            raise ValidationError(_("Erreur de format pour le champ 'nom'"))
        return data

class AddMachineForm(forms.Form):
    nom = forms.CharField(required = True, label = 'Nom de la machine')
    def clean_nom (self) :
        data = self.cleaned_data ["nom"]
        if len(data) != 6:
            raise ValidationError (_("Erreur de format pour le champ nom"))
        return data

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)