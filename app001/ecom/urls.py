from django.urls import path
from . import views 

app_name = "ecom"

urlpatterns = [
    path("", views.index, name="index"),
    path("product/", views.product_list, name="shop"),
    path("cat/", views.category_list, name="cat"),
    path("cat/<str:slug>", views.category_detail, name="cat-detail"),
    path("product/<str:slug>", views.product_detail, name="product-detail"),
]
