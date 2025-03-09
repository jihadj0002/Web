from django.urls import path
from . import views

app_name = "insta"

urlpatterns = [
    path("", views.view_profile, name="index"),
    path("profile/", views.view_profile, name="view_profile"),
    
    path('oauth/instagram/', views.instagram_oauth, name='instagram_oauth'),
    path('oauth/instagram/callback/', views.instagram_callback, name='instagram_callback'),

]
