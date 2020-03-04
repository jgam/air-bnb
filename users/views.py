from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form_is_valid():
            print(form.cleaned_data)
        print(dir(form))
