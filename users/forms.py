from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # clean method cleans the data and returns None as default
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        print("clean passwords")
