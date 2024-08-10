import requests
from django.shortcuts import render

def chatbot_view(request):
    answer = ""
    if request.method == 'POST':
        gptapi = "aCgLh48181706506halwh"
        question = request.POST.get("title", "")
        text = question.replace(' ', '+')

        # ارسال درخواست به API شخص ثالث
        response = requests.get(
            f"https://gpt.irateam.ir/api/web.php",
            params={
                "apikey": gptapi,
                "type": "freegpt5",
                "question": text
            }
        )

        if response.status_code == 200:
            json_response = response.json()
            answer = json_response.get("results", {}).get("answer", "")

            # ذخیره پاسخ در فایل (برای شبیه‌سازی رفتار اصلی)
            with open("que.txt", "w") as file:
                file.write(answer)
        else:
            answer = "خطا در دریافت پاسخ از سرور"

    return render(request, 'chatbot/chat_form.html', {'answer': answer})


# Create your views here.
