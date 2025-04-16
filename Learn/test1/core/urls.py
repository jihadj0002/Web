from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    
    path("shop/", views.shop, name="shop"),
    path("product/<slug>", views.view_product, name="view_product"),
    
    
    path("cat/", views.categories, name="cat"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("cart/", views.cart, name="cart"),
    
]
