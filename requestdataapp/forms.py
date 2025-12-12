from django import forms

class UserBioForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Age', min_value=0, max_value=120)
    bio = forms.CharField(label='Bio', widget=forms.Textarea)