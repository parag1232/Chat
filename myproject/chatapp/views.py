from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def _login(request):
    context = {'key':'value' }
    return render(request,'chatapp/login.html',context=context)



def signUp(request):
    form = UserCreationForm()
    return render(request,'chatapp/signupPage.html')    