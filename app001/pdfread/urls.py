from django.urls import path
from . import views

app_name="pdfread"

urlpatterns = [
    path("", views.index, name="index"),
    path("read/<int:pdf_id>", views.read_book, name="read"),
    path("up/", views.upload_pdf, name="upload"),
 
]
