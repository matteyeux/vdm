from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def index(response):
	return render(response, "index.html", {})


def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("/homepage")
	else:
		form = RegisterForm()

	return render(response, "register/register.html", {
			"form": form
		})
