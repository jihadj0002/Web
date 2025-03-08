from django.urls import path
from . import views

app_name = 'ai'

urlpatterns = [
    path("ds/", views.deepseek_api, name="deepseek_api"),
    path("", views.index, name="index"),
    
] 
