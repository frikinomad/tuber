from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        #here this user will be available for all the templates in the templates folder without even passing via the data in return render() as we have done in the past

        if user is not None:
            auth.login(request, user)       #above authenticate just verify the credentials and login allow them to enter the site
            messages.warning(request, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        #these below names should be same as name given in the form to the input fields
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            #we can add things like, username email should be unique in db, password should be x characters long and etc
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password) #here User is our db and create_user is query,
                    #and all in bracket our the things we are storing, notice we are not storing confirm_password
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'Password do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')

@login_required(login_url='login')      #now we cannot access the dashboard without being logged in
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout_user(request):
    logout(request)
    return redirect('home')

