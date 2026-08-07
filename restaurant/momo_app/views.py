from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        message=request.POST['message']
        Form.objects.create(name=name,email=email,number=number,message=message)
        return redirect('index')
    return render(request,'momo_app/index.html')  

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