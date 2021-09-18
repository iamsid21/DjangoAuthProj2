from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')
    print(userName,passWord)
    # check if user is loogin in with correct credentials
    user = authenticate(username=userName, password=passWord)
    if user is not None:
        # A backend authenticated the credentials
        login(request,user)
        return redirect('/')
    else:
        # No backend authenticated the credentials
        return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login") 