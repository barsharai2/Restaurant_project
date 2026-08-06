from django.shortcuts import render

# Create your views here.
def index(request):
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