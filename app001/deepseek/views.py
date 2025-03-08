from django.http import JsonResponse
from django.conf import settings
from openai import OpenAI
import requests
import json

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
                    "content": "Tell me more about This Universe?"
                }
            ]
        )
        response_content = completion.choices[0].message.content
        return JsonResponse({"response": response_content}, safe=False)
    except Exception as e:
        print("OpenRouter API Error:", e)
        return JsonResponse({"error": str(e)}, status=500)
    