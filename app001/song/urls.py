from django.urls import path
from . import views

app_name = "song"

urlpatterns = [
    path("", views.index, name="index"),
    path("song/<int:id>", views.detail, name="detail"),
]
