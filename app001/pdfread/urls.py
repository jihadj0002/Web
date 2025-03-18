from django.urls import path
from . import views

app_name="pdfread"

urlpatterns = [
    path("", views.index, name="index"),
]
