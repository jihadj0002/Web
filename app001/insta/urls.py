from django.urls import path
from . import views

app_name = "insta"

urlpatterns = [
    path("", views.view_profile, name="view_profile"),
]
