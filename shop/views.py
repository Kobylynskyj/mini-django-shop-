from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    context = {
        'date': datetime.now(),
    }
    return render(request, "shop/index.html",context)

def about(request):
    context = {
        'date': datetime.now(),
    }
    return render(request, "shop/about.html",context)


def contact(request):
    context = {
        'date': datetime.now(),
    }
    return render(request, "shop/contacts.html",context)

def product_list(request):
    context = {
        'date': datetime.now(),
    }
    return render(request, "shop/products.html",context)

def product_detail(request,pk):
    context = {
        'date': datetime.now(),
    }
    return   render(request, "shop/product_detali.html",context)

def login_view(request):
    context = {
        'date': datetime.now(),
    }
    return render(request, "shop/login_view.html", context)

def register_view(request):
    context = {
        'date': datetime.now(),
    }
    return render(request, "shop/register_view.html", context)

def logout_view(request):
    context = {
        'date': datetime.now(),
    }
    return HttpResponse("выход из аккаунта", content)

