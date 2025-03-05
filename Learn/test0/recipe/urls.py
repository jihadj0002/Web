from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path("", views.index, name="index"),
    
    path("view/<int:pk>", views.detail, name="detail"),
    path("update/<int:pk>", views.update_recipe, name="update_recipe"),
    path("delete/<int:pk>", views.delete_recipe, name="delete_recipe"),
    
    
    path("login/", views.login, name="login"),
    path("logout/", views.logoutt, name="logout"),
    path("signup/", views.signup, name="signup"),
    
]
