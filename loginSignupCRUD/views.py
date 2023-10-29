from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user!=None:
            login(request,user)
            return redirect("index")
        else:
            return HttpResponse("username not found")
        
    return render(request, 'login.html')

def index(request):
    # user=request.user
    # userdata=user.objects.all()
    users = User.objects.all()
    context={
         'user':users   
    }
    return render(request, 'index.html', context)



def addUser(request):
    
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
            return redirect('index')
    
    return render(request, 'addUser.html')


def deleteUser(request,id):
    user=User.objects.filter(id=id)
    user.delete()
    return redirect("index")


# def updatePage(request, id):
    user=User.objects.get(id=id)
    context={
        'user': user
    }
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')

        update= User(
            id = id,
            username = username,
            first_name = fname,
            last_name=lname,
            email = email 
        )

        update.save()
        return redirect("index")
    
    return render(request, "update.html", context)


def updatePage(request, id):
    # Retrieve the user based on the provided ID
    user = User.objects.get(id=id)
    
    if request.method == "POST":
        # Get updated data from the form
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')

        # Update the user's fields
        user.username = username
        user.first_name = fname
        user.last_name = lname
        user.email = email

        # Save the changes
        user.save()
        
        return redirect('index')
    
    context = {
        'user': user
    }
    return render(request, "update.html", context)