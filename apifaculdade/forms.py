from django import forms

class SenhaForm(forms.Form):
  senha = forms.CharField(label='Senha', max_length=100)