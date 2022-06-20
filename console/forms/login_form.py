from cProfile import label
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Manager Email', max_length=200) 
    password = forms.CharField(label='password', widget=forms.PasswordInput)