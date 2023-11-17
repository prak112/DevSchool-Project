from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label="Enter search like 'Mountains near a river'")
    