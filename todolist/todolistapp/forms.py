from django import forms


class createlist(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    check = forms.BooleanField(label='Completed')
