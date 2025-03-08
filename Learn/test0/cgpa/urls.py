from django.urls import path
from . import views

app_name = "cgpa"

urlpatterns = [
    path("", views.index, name="index"),
    path("result/", views.result, name="result"),
    path("edit/<int:pk>", views.edit_sub, name="edit_sub"),
    path("del/<int:pk>", views.delet, name="delete"),
] 
