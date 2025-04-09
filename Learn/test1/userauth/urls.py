from . import views 
from django.urls import path

app_name = "userauth"

urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    # path("update_profile/", views.update_profile, name="update_profile"),
]