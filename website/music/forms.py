from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):

# widget is use to save the password as a password field in the DB
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
