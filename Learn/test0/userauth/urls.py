from django.urls import path
from .import views

app_name ="userauth"

urlpatterns = [
    
    path("login/", views.login, name="login"),
    path("logout/", views.logoutt, name="logout"),
    path("signup/", views.signup, name="signup"),
    
]
