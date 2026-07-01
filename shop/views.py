from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Главная страница магазина")

def about(request):
    return HttpResponse("О нас")

def contact(request):
    return HttpResponse("страница с контактами")

def product_list(request):
    return HttpResponse("список всех товаров")

def product_detail(request,pk):
    return HttpResponse(f"Товар с id {pk}")

def login_view(request):
    return HttpResponse("Вход")

def register_view(request):
    return HttpResponse("Регистрация")

def logout_view(request):
    return HttpResponse("выход из аккаунта")