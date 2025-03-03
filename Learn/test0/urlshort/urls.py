from django.urls import path
from . import views

app_name = "urlshort"

urlpatterns = [
    path("", views.index, name="index"),
    path("url/<str:slug>", views.view_url, name="view_url"),
    path("url/open/<str:slug>", views.url_redirect, name="url_redirect"),
]
