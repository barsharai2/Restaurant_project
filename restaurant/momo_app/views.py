from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import qrcode
import re
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def index(request):
    category=Category.objects.all()
    cateid=request.GET.get('category')
    if cateid=='all':
        momo=Momo.objects.filter(is_available=True)
    elif cateid:
        momo=Momo.objects.filter(is_available=True,category=cateid)
    else:
        momo=Momo.objects.filter(is_available=True)
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        message=request.POST['message']
        Form.objects.create(name=name,email=email,number=number,message=message)
        messages.success(request,f"{name} Your form is successful submitted ")
        # request.session
        response= redirect('index')
        response.set_cookie('name',name,max_age=3600)
        return response

    context={'category':category,
             'momo':momo
             }
    return render(request,'momo_app/index.html',context)  

def contact(request):
    return render(request,'momo_app/contact.html')

def about(request):
    return render(request,'momo_app/about.html')

@login_required(login_url='login_part')
def menu(request):
    category=Category.objects.all()
    qr=qrcode.make("http://127.0.0.1:8000/menu/")
    qr.save('momo_app/static/images/qr.png')
    context={
        'category':category
    }
    return render(request,'momo_app/menu.html',context)

def services(request):
    return render(request,'momo_app/services.html')

def testemonial(request):
    teste=Momo.objects.all()
    review=Review.objects.all()
    if request.method == "POST":
        name=request.POST['name']
        rating=request.POST['rating']
        order=request.POST.get('order')
        message=request.POST['message']
        Review.objects.create(name=name,rating=rating,order=order,message=message)
        messages.success(request,f"{name} Your form is successful submitted ")


    context={'momos':teste,
             'review':review}
    return render(request,'momo_app/testemonial.html',context)
def term(request):
    return render(request,'momo_app/terms.html')

'''
============================================================================================
============================================================================================
                                         AUTH
============================================================================================
=============================================================================================

'''
def login_part(request):
    name=request.COOKIES.get('name')
    if request.method == 'POST':
    
        username=request.POST.get("username")
        password=request.POST.get("password")
        remember_me=request.POST.get("remember_me")

        if not User.objects.filter(username=username).exists():
            messages.error(request,"username is incorrect")
            return redirect('login_part')
        
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if remember_me:
                request.session.set_expiry(360000)
            else:
                request.session.set_expiry(0)
            next=request.POST.get('next','')
            return redirect(next if next else "index")
        else:
            messages.error(request,"password is incorrect")
            return redirect("login_part")
                
        
    next=request.GET.get('next','')
    return render(request,'auth/login.html',{'next':next,'name':name})

def register(request):
    if request.method == 'POST':
            fname=request.POST['firstname']
            lname=request.POST['lastname']
            uname=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            password1=request.POST['password1']
            print("check")
            if password==password1:
                if User.objects.filter(username=uname).exists():
                    messages.error(request,"username is already exists")
                    return redirect('register')
                if User.objects.filter(email=email).exists():
                    messages.error(request,"email is already exists")
                    return redirect('register')
                if not re.search(r"[A-Z]",password):
                    messages.error(request,"password msut contain at least one uppercase")
                    return redirect('register')
                if not re.search(r"\d",password):
                   messages.error(request,"password msut contain at least one digit")
                   return redirect('register')

                try:
                    user=User(first_name=fname,username=uname)
                    validate_password(password,user=user)
                    User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
                    messages.success(request,"Your account is successfully register")
                    return redirect ('register')
                except ValidationError as e:
                    for i in e.messages:
                        messages.success(request,i)
                    return redirect('register')
                
            else:
                messages.error(request,"password and confirm password is incorrect !!")
                return redirect('register')
        
    return render(request,'auth/register.html')

def log_out(request):
    logout(request)
    return redirect('login_part')

@login_required(login_url='login_part')
def pass_change(request):
    form=PasswordChangeForm(user=request.user)
    if request.method =='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_part')
    return render(request,'auth/password_change.html',{'form':form})