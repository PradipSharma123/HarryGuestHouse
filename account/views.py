from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['Username']
        password1 = request.POST['password']
        confirmpassword = request.POST['cpassword']

        if password1 == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,  'Username Already Taken')
            else:
                user = User.objects.create_user(username=username,
                                                password=password1,
                                                first_name=fname,
                                                last_name=lname)
                user.save()
                messages.info(request, 'The user has been registered')
                return redirect('/accounts/login/')
        else:
            messages.info(request, 'Password doesnot match ')
        return redirect('/accounts/register/')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/accounts/dashboard/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('/accounts/login/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/index/')


def dashboard(request):
    return render(request, 'dashboard.html')
