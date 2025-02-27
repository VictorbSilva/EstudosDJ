from django import forms
from .models import cepModel

class cepForm(forms.ModelForm):
    class Meta:
        model = cepModel
        fields = ['cep']