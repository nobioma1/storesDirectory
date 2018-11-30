from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=200, required=True)
    lastname = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ("firstname", "lastname", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)

        user.firstname = self.cleaned_data["firstname"]
        user.lastname = self.cleaned_data["lastname"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user
