from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("portfolio", views.porfolio, name="portfolio"),
    path("services", views.services, name="services"),
    path("resume", views.resume, name="resume"),
    path("contact", views.contact, name="contact"),
    
]


# about
# porfolio
# services
# resume
# contact