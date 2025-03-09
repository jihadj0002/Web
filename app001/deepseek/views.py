from django.http import JsonResponse
from django.conf import settings
from openai import OpenAI
from hiking.models import Content
import requests
import json


api_key="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",

text = Content.objects.get(id=190).body



def deepseek_api(request):
    pass



def index(request):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )
     

    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Replace with your site URL.
                "X-Title": "<YOUR_SITE_NAME>",      # Optional. Replace with your site name.
            },
            model="deepseek/deepseek-r1-distill-llama-70b:free",
            messages=[
                {
                    "role": "user",
                    "content": f"here is some text {text} Now modify this with something good and mention @hike_camp__"
                }
            ]
        )
        response_content = completion.choices[0].message.content
        return JsonResponse({"response": response_content}, safe=False)
    except Exception as e:
        print("OpenRouter API Error:", e)
        return JsonResponse({"error": str(e)}, status=500)
    

def index1(request):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        
    )
     

    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Replace with your site URL.
                "X-Title": "<YOUR_SITE_NAME>",      # Optional. Replace with your site name.
            },
            model="deepseek/deepseek-r1-distill-llama-70b:free",
            messages=[
                {
                    "role": "user",
                    "content": "Tell me more about This Universe?"
                }
            ]
        )
        response_content = completion.choices[0].message.content
        return JsonResponse({"response": response_content}, safe=False)
    except Exception as e:
        print("OpenRouter API Error:", e)
        return JsonResponse({"error": str(e)}, status=500)
    