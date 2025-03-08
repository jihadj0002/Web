from django.urls import path
from . import views

app_name = 'hiking'

urlpatterns = [
    path("", views.index, name="index"),
]
