from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    category=Category.objects.all()
    cateid=request.GET.get('category')
    if cateid:
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
    return render(request,'momo_app/menu.html')

def services(request):
    return render(request,'momo_app/services.html')

def testemonial(request):
    return render(request,'momo_app/testemonial.html')
def term(request):
    return render(request,'momo_app/terms.html')