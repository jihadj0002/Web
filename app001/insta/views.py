from django.shortcuts import render, HttpResponse
import requests
import json


# Create your views here.
def view_profile(request):
    
    # domain = "https://graph.instagram.com/v22.0/"
    
    # my_username = "hike_camp__"
    
    # part_a = "me?field=id,name,username,account_type,media_count,ig_id"
    
    # access_token = "&access_token=EAAQzduZBkpZCQBOzrFH4pW54mu5qtm1VbRsK7hat05rWs1cacLRigDPZCEttT6N2diQuTE6Q4aaJQP7pRlSMWDKLhdDPcduglFpe6nhWNUuZBteNf5oLhlwd9FHxWrBIY5tpdcqJUFOqcyuwOqQ2cqKjDvr2uZBq6r51ZCeDlmR4J4Ft5k1HwkTTOYqXpAZBbyKGySbc6ZBxRprikIbM0DC9vkjMUf8ZD"
    
    # box = []
    # i=0
    # while i<10:
    #     part_b = "media?fields=id,caption,media_type,media_url,thumbnail_url,permalink,timestamp,username&limit=10&after="
    #     url = domain + part_a + str(i) + access_token
    #     response = requests.get(url)
    #     #data = json.loads(response.text)
    #     #box.append(data)
    #     i+=10
        
    return HttpResponse("Hello World")