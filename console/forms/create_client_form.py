from django import forms

class CreateClientForm(forms.Form):
    client_name = forms.CharField(label='Client Name', max_length=100)
    client_company = forms.CharField(label='client Company', max_length=100)
    client_email = forms.EmailField(label='Client Email', max_length=200)