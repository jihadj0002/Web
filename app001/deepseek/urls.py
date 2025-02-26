from django.urls import path
from . import views

app_name = 'deepseek'

urlpatterns = [
    path("", views.deepseek_api, name="index"),
    
]
