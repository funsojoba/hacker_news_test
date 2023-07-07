from django import forms


class NewsSearchForm(forms.Form):
    q = forms.CharField(label='Search')