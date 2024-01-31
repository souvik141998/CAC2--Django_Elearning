from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is Homepage")

def about(request):
   return render(request,'aboutUs.html')

def stdash(request):
    return render(request,'stdashboard.html')

def trdash(request):
    return render(request,'teacherDashboard.html')

def auth(request):
    return render(request,'login.html')

def registerr(request):
    return render(request,'register.html')



#login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('dash')
            elif user.is_staff:
                return redirect("trdash")
            else:
                return redirect("stdash")
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return redirect('login')

#register view
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # gender = request.POST['gender']
        # education = request.POST['education']
        # phone = request.POST['phone']
        if User.objects.filter(username=username).exists():
            messages.info(request,"user already exist")
            return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return render(request,'register.html')
        else:
          user=User.objects.create_user(username=username,email=email,password=password)
          user.save();
        return redirect('login')
    else:
     return render(request,'register.html')

       