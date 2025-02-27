from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.product_list, name="shop"),
]
