from django.forms import forms

class ClientUploadForm(forms.Form):
    file = forms.FileField()