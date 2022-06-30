from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here. 

def signin(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'GET':
        return render(request=request, template_name='authentication/signin.html')

    elif request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('add') 
            #return render(request=request, template_name='entries/add.html')

        else:
            messages.error(request, "Bad credentials!")
            return redirect('signin')



def register(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'GET':
        return render(request=request, template_name='authentication/register.html')

    elif request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exixts! Please try some other username")
            return redirect('register')

        elif User.objects.filter(email=email):
            messages.error(request, "email already registered!")
            return redirect('register')

        elif len(username)>10:
            messages.error(request, "Username cannot exceed ten characters")

        elif pass1 != pass2:
            messages.error(request, "Password didn't matcth!")

        elif not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('register')


        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.is_active = True
            myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')

def logout_request(request):
    logout(request)
    return redirect('signin')
        

