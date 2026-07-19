from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1000.00
    )


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Замовлення {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Purchase(models.Model,):
    order_item = models.OneToOneField(OrderItem, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Покупка {self.order_item.product.name}"