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
    if request.method == "POST":
        name=request.POST['name']
        rating=request.POST['rating']
        order=request.POST.get('order')
        message=request.POST['message']
        Review.objects.create(name=name,rating=rating,order=order,message=message)

    context={'momos':teste}
    return render(request,'momo_app/testemonial.html',context)
def term(request):
    return render(request,'momo_app/terms.html')