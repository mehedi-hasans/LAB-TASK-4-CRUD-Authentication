from django.shortcuts import render

def signupPage(request):
    return render(request, 'signup.html')

def loginPage(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')