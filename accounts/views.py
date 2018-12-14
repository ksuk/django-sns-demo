from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login/")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})          


def thanks(request):
    return render(request, "accounts/thanks.htmls")    