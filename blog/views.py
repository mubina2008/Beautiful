from django.shortcuts import render
from .models import Pudra,Products,Customers
# Create your views here.
def asosiypage (request):


    return render(request,  'index.html',context = context )

def about(request):
    return render(request,'about.html',context={})

def client(request):
    return render(request,'client.html',context={})


def index(request):
    customers = Customers.objects.all()
    pudra = Pudra.objects.all()
    context = {
        'pudra': pudra,
        'customers': customers

    }
    return render(request,'index.html',context=context)

def products(request):
    products = Products.objects.all()
    context = {
        products : 'products'
    }

    return render(request,'products.html',context=context)

def contact(request):
    return render(request,'contact.html', context={})



