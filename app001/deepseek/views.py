from django.http import JsonResponse
from django.conf import settings
from openai import OpenAI

def deepseek_api(request):
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
                    "content": "What is the meaning of life?"
                }
            ]
        )
        response_content = completion.choices[0].message.content
        return JsonResponse({"response": response_content}, safe=False)
    except Exception as e:
        print("OpenRouter API Error:", e)
        print("Error sakndjas")
        return JsonResponse({"error": str(e)}, status=500)