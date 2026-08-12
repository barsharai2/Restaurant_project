from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import qrcode
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

        return redirect('index')

    context={'category':category,
             'momo':momo
             }
    return render(request,'momo_app/index.html',context)  

def contact(request):
    return render(request,'momo_app/contact.html')

def about(request):
    return render(request,'momo_app/about.html')

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
    return render(request,'auth/login.html')

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
                pass
            else:
                messages.error(request,"password and confirm password is incorrect !!")
                return redirect('register')
        
    return render(request,'auth/register.html')