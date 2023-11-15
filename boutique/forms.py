from django import forms
from boutique.models import Article

class FormConnexion(forms.Form):
    login= forms.CharField(max_length=30)
    mot2pass = forms.CharField (widget=forms.PasswordInput)


class Search(forms.Form):
    prod = forms.CharField(max_length=30)
    prix= forms.FloatField()
    stat=forms.CharField(max_length=30)
    dateCmd=forms.DateField()
