from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
import requests

def home(request: WSGIRequest):
    return render(request, 'home.html')

def about(request: WSGIRequest):
    return render(request, 'about.html')

def skills(request: WSGIRequest):
    return render(request, 'skills.html')

def portfolio(request: WSGIRequest):
    return render(request, 'portfolio.html')

def contact(request: WSGIRequest):
    return render(request, 'contact.html')

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        token = "7456811289:AAGnos7xI27HB1xBjKnZJJBIL3qDich_bWM"
        chat_id = "6150504681"
        telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"

        data = {
            'chat_id': chat_id,
            'text': f"<b>Name:</b> {name}\n<b>Email:</b> {email}\n<b>Message:</b> {message}",
            'parse_mode': 'html'
        }

        response = requests.post(telegram_url, data=data)
        result = response.json()

        if result.get("ok"):
            return render(request, 'success.html')
        else:
            return render(request, 'unsuccessful.html')

    return render(request, 'unsuccessful.html')

