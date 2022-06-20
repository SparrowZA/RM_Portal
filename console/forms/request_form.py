from django import forms

class RequestForm(forms.Form):
    client = forms.CharField(widget=forms.HiddenInput())
    doc_name = forms.CharField(label='Document Name', max_length=100)
