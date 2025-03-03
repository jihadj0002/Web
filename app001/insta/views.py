from django.shortcuts import render, HttpResponse
import requests
from rest_framework.response import Response
import json


# Create your views here.
def view_profile(request):
    
    domain = "https://graph.facebook.com/v22.0/"
    
    my_username = "hike_camp__"
    fields = "id,name,short_name,education"
    
    
    access_token = "EAAQzduZBkpZCQBOZBNkoBZA0DNJSzMZBcIJt5u8fccTbCk8bua048O744xk8FdOlrAYKRNHx2eKo7clPJwsavR55fzyK7FiLNUpEGu01R1fEPRQQAwCWraLt17uIIY7hmJ16DpqSrl2shz8IgBHM1cQ1NenXfMQZAtuCdbpux1wOgtb2e7JOsbX4dEPldMonh8fCTebaSEWeRIGE97bRXUvm78m2gZD"
    
    url = f"{domain}me?fields={fields}&access_token={access_token}"
    
    response = requests.get(url)
    data = response.json()
    print(data)
    
    context = {
        "data":data,
    }
    return render(request, "insta/profile_view.html", context)
    #return HttpResponse(data)