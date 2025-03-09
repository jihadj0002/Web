from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from .models import InstagramAccount
from django.http import JsonResponse
import json


# Create your views here.

INSTAGRAM_OAUTH_URL = "https://api.instagram.com/oauth/authorize"
INSTAGRAM_ACCESS_TOKEN_URL = "https://api.instagram.com/oauth/access_token"




@login_required
def instagram_oauth(request):
    
    client_id = settings.INSTAGRAM_CLIENT_ID
    redirect_uri = 'insta:instagram_callback'
    scope = "user_profile,user_media"
    
    oauth_url = f"{INSTAGRAM_OAUTH_URL}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code"
    
    return redirect(oauth_url)

@login_required
def instagram_callback(request):
        
        code = request.GET.get('code')
        
        if not code:
            return HttpResponse("Code not found")
        
        client_id = settings.INSTAGRAM_CLIENT_ID
        client_secret = settings.INSTAGRAM_CLIENT_SECRET
        redirect_uri = 'insta:instagram_callback'
        
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': code,
        }
        
        response = requests.post(INSTAGRAM_ACCESS_TOKEN_URL, data=data)
        if response.status_code != 200:
            access_token = response.json()
            
            user_info = response.json().get('user')
            
            InstagramAccount.objects.create(
                user = request.user,
                username = user_info.get('username'),
                access_token = access_token.get('access_token')
            )
        
            print(access_token)
            return redirect('insta:index') # Redirect to the dashboard Create a new Dashboard view
        else:
            return redirect('insta:index') # Redirect to the Error Page Create a new Dashboard view
        
    

def get_user_profile(request):
    access_token = "EAAQzduZBkpZCQBOxe31rjIfLvziKX2GX8S2div6YnqT1hEZAtbQrH2kF9bZCL74S9gvMFP0uA1XxvLl8HWoTNlo8onXgBbd8VK5oFIETIHjThDKmNFCrDW5lGDcBw4eGDZBAdlaErZALKRq2pdiTNfxTYi2DFCvzL9Sb7pZA0qw8jjyVr3cBt6xTRMBog3AKRiVOdRs3zmcX8ZCysMncIPSIdT2FhM0ZD"  # Replace with actual access token
    url = f"https://graph.facebook.com/v22.0/me?fields=id&access_token={access_token}"
    
    # Send GET request to Instagram Graph API
    response = requests.get(url)
    
    # Check if the response status code indicates success
    if response.status_code == 200:
        try:
            # Attempt to parse the JSON response
            user_profile = response.json()
            return JsonResponse(user_profile)  # Return the profile data as a JSON response
        except ValueError:
            # Handle the case where JSON is invalid or empty
            return JsonResponse({"error": "Failed to decode JSON response from Instagram API."}, status=500)
    else:
        # Handle unsuccessful response status codes
        return JsonResponse({"error": f"Request failed with status {response.status_code}.", "response": response.text}, status=response.status_code)
    
    
def index(request):
    return render(request, "insta/index.html")


def upload_media(access_token, media_url, caption):
    domain = "https://graph.facebook.com/v22.0/"
    
    url = f"{domain}me/media?access_token={access_token}"
    
    data = {
        "image_url": media_url,
        "caption": caption
    }
    
    response = requests.post(url, data=data)
    return response.json()

def view_profile(request):
    
    domain = "https://graph.facebook.com/v22.0/"
    
    my_username = "hike_camp__"
    fields = "id,name,short_name,education"
    
    access_token = "EAAQzduZBkpZCQBOxe31rjIfLvziKX2GX8S2div6YnqT1hEZAtbQrH2kF9bZCL74S9gvMFP0uA1XxvLl8HWoTNlo8onXgBbd8VK5oFIETIHjThDKmNFCrDW5lGDcBw4eGDZBAdlaErZALKRq2pdiTNfxTYi2DFCvzL9Sb7pZA0qw8jjyVr3cBt6xTRMBog3AKRiVOdRs3zmcX8ZCysMncIPSIdT2FhM0ZD"
    
    url = f"{domain}me?fields={fields}&access_token={access_token}"
    
    response = requests.get(url)
    data = response.json()
    print(data)
    
    context = {
        "data":data,
    }
    return render(request, "insta/profile_view.html", context)
    #return HttpResponse(data)