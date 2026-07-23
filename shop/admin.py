from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem, Purchase

# Register your models here.

class CustomProduct(admin.ModelAdmin):
    list_display = ["name", "price", "category", "created_date"]
    list_filter = ["category"]
    search_fields = ["name", "description"]


class CustomCategory(admin.ModelAdmin):
    list_display = ["name", "created_date"]
    search_fields = ["name"]


class CustomOrder(admin.ModelAdmin):
    list_display = ["id", "user", "total_price", "created_date"]
    list_filter = ["user"]
    search_fields = ["user__username"]



admin.site.register(Category, CustomCategory)
admin.site.register(Product, CustomProduct)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, CustomOrder)
admin.site.register(OrderItem)
admin.site.register(Purchase)

