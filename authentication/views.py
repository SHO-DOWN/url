from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate,login as Login
# Create your views here.


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # handle login
            if request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    userAuthenticate = authenticate(username=user,password=request.POST['password'])
                    # auth.login(request, userAuthenticate)
                    if userAuthenticate is not None:
                        Login(request,user)
                        return redirect(request.POST.get('next'))
                    else:
                        messages.error(request,'Wrong Password')
                        return render(request,'login.html',{'error': "Wrong Password"}) 
                except User.DoesNotExist:
                    messages.error(request,"User Doesn't Exist")
                    return render(request, 'login.html', {'error': "User Doesn't Exist"})
            else:
                return render(request, 'login.html', {'error': "Empty Fields"})
        else:
            return render(request, 'login.html')
    else:
        return redirect('/')


def signup(request):
    if request.method == "POST":
        # handle sign in
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    return render(request, 'signup.html', {'error': "User Already Exists"})
                except User.DoesNotExist:
                    User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'],
                    )
                    messages.success(
                        request, "Signup Successful!Login Here")
                    return redirect(login)
            else:
                return render(request, 'signup.html', {'error': "Empty Fields"})
        else:
            return render(request, 'signup.html', {'error': "Password's Don't Match"})
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')
