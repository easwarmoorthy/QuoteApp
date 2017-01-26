from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from .models import *
from .forms import *
def index(request):
	return HttpResponse("Done!!!")

def login_view(request):
	print("Login:")
	print(request.user.is_authenticated())
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username="username",password="password")
		login(request,user)
		print(request.user.is_authenticated())
	return render(request, "quoteapp/form.html", {"form":form})

def quote_view(request):
	form = QuoteForm(request.POST or None)
	if form.is_valid():
		quote = form.cleaned_data["quote"]
		qname = form.cleaned_data["qname"]
		new_quote = form.save(commit=False)
		new_quote.save()
		return render(request,"quoteapp/quote.html",{"form":form})
	all_quotes = QuoteModel.objects.all()
	print(all_quotes)
	context = {"form":form,"all_quotes":all_quotes}
	return render(request,"quoteapp/quote.html",context)

def register_view(request):
	print(request.user.is_authenticated())
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		#login(request,user)
	return render(request,"quoteapp/form.html",{"form":form})

def logout_view(request):
	logout(request)
	return HttpResponse("Logged out")
