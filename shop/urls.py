from django.urls import path
from shop.views import index,about,contact,product_list,product_detail,login_view,register_view,logout_view
urlpatterns = [
    path('', index, name="home_page"),
    path('about/', about, name="about"),
    path('contacts/', contact, name="contacts"),
    path('products/', product_list, name="products"),
    path('products/<int:pk>', product_detail, name="product_detail"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('logout/', logout_view, name="logout_view"),
]