from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def signupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmpassword')

        if pass1!=pass2:
            return HttpResponse('Not Match')
        
        else:
            myuser=User.objects.create_user(uname,email,pass1)
        myuser.save()
        return redirect('loginPage')

    return render(request, 'signup.html')




def loginPage(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')