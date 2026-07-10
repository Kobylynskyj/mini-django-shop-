from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "shop/index.html")

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return render(request, "shop/contacts.html")

def product_list(request):
    return render(request, "shop/products.html")

def product_detail(request,pk):
    return   render(request, "shop/product_detali.html")

def login_view(request):
    return render(request, "shop/login_view.html")

def register_view(request):
    return render(request, "shop/register_view.html")

def logout_view(request):
    return HttpResponse("выход из аккаунта")