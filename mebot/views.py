from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TelegramUser
from .serializers import TelegramUserSerializer
from .utils import send_message, get_chat, get_me  # Import relevant functions
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TelegramUser, Update, UserState, Membership, Admin
from .serializers import UpdateSerializer
from .utils import send_message, get_chat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Channel, Message
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from ipaddress import ip_address

# تعریف محدوده‌های IP تلگرام
TELEGRAM_IP_RANGES = [
    ('149.154.160.0', '149.154.175.255'),
    ('91.108.4.0', '91.108.7.255'),
]


# تابع کمکی برای بررسی محدوده IP
def is_ip_in_range(ip, ip_range):
    lower, upper = ip_range
    return ip_address(ip) >= ip_address(lower) and ip_address(ip) <= ip_address(upper)


def check_ip(request):
    # دریافت آدرس IP کاربر
    client_ip = request.META.get('REMOTE_ADDR', '')

    # بررسی اینکه آیا IP در هر یک از محدوده‌های تعریف شده است
    is_allowed = any(is_ip_in_range(client_ip, ip_range) for ip_range in TELEGRAM_IP_RANGES)

    if not is_allowed:
        return HttpResponse("Sik :)", status=403)

    return HttpResponse("Hello, Telegram!", status=200)



class UpdateView(APIView):
    def post(self, request):
        # Parse update data from Telegram
        update_data = request.data
        chat_id = update_data.get('message', {}).get('chat', {}).get('id')

        # Check if user exists or create a new one
        user, created = TelegramUser.objects.get_or_create(chat_id=chat_id)
        if created:
            # Save additional user information if available (username, etc.)
            user.username = update_data.get('message', {}).get('from', {}).get('username')
            user.first_name = update_data.get('message', {}).get('from', {}).get('first_name')
            user.last_name = update_data.get('message', {}).get('from', {}).get('last_name')





@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        # Parse the incoming Telegram update
        data = request.json()
        message = data.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        text = message.get('text', '')

        # Handle the "/start" command
        if text == '/start':
            return start_command(chat_id)

        # Handle the "/conect" command
        elif text == '/conect':
            return conect_command(chat_id)

        # Handle other messages
        else:
            return handle_message(chat_id, text)

    return JsonResponse({'status': 'not a post request'})


def start_command(chat_id):
    # Add user if not already in database
    user, created = User.objects.get_or_create(telegram_id=chat_id)

    # Send welcome message
    response = {
        'chat_id': chat_id,
        'text': (
            "سلام کاربر عزیز 🌹\n"
            "🌿 به ربات تامین ستاد خوش آمدید.\n"
            "---روی کد لمس کنید تا کپی بشه--\n"
            "-=-=-=-----=-=-----=-=-=-=\n"
            f"<code>{chat_id}</code>\n"
            "-=-=-=-------------=-=-=-=-=\n"
            "کد بالا جهت ثبت سفارش و دریافت اعلان آگهی ها توسط این ربات برای شما ارسال شده است\n"
            "💎 برای ورود به فرم از این لینک وارد شوید\n"
            "https://bahooshansite.ir"
        ),
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [
                [{'text': "اخبار سایت", 'callback_data': "blog"},
                 {'text': "جدیدترین آگهی ها", 'callback_data': "none"}],
                [{'text': "ارتباط با پشتیبانی 👤", 'callback_data': "4"}]
            ],
            'resize_keyboard': True
        }
    }
    return JsonResponse(response)


def conect_command(chat_id):
    # Send connection information
    response = {
        'chat_id': chat_id,
        'text': (
            "<code>https://sub.iprostable.enterprises/subscribe/mixed/ZHc3aXVuNGhuZGFpMXZ1cDpjUkQxcnJQSkJ0SFV0WjJV</code>\n"
            "کانفیک جهت اتصال\n"
            "جهت دریافت آموزش و همچنین فایل نصبی می‌توانید از اینجا دریافت نمایید\n"
            "<a href='https://t.me/taminsetad.com/110'>کانکشن</a>\n"
            "----------------\n"
            "@taminsetadcombot"
        ),
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [
                [{'text': "🧞‍♂️ ربات ها", 'callback_data': "aghahi"},
                 {'text': "⭐جوایز و مسابقات", 'callback_data': "7"}],
                [{'text': "🌐هوش مصنوعی", 'callback_data': "4"}, {'text': "🐘 کانکشن قدرتمند", 'callback_data': "5"}],
                [{'text': "🦋توییتریسم با شما", 'callback_data': "4"},
                 {'text': "❇ یک ربات بسازید", 'callback_data': "5"}],
                [{'text': "ارتباط با پشتیبانی 👤", 'callback_data': "4"}]
            ],
            'resize_keyboard': True
        }
    }
    return JsonResponse(response)


def handle_message(chat_id, text):
    # Default response for unhandled messages
    response = {
        'chat_id': chat_id,
        'text': "پیام شما دریافت شد، اما ما نمی‌دانیم چگونه پاسخ دهیم.",
    }
    return JsonResponse(response)

# bot/views.py



@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        text = message.get('text', '')

        # Check if it's a callback query
        callback_query = data.get('callback_query', {})
        if callback_query:
            chat_id = callback_query['message']['chat']['id']
            data = callback_query.get('data', '')
            callback_id = callback_query['id']
            message_id = callback_query['message']['message_id']
            return handle_callback(chat_id, data, callback_id, message_id)

        # Fetch user or create new
        user, created = User.objects.get_or_create(telegram_id=chat_id)

        # Check if user is blocked
        if user.blocked:
            return blocked_user_response(callback_query.get('id', ''))

        # Handle specific commands
        if text == '/start':
            return start_command(chat_id, user)

        elif text == '/connect':
            return connect_command(chat_id)

        # Handle other messages or commands
        return default_response(chat_id)

    return JsonResponse({'status': 'not a post request'})

def blocked_user_response(callback_query_id):
    response = {
        'method': 'answerCallbackQuery',
        'callback_query_id': callback_query_id,
        'text': "شما از بات بلاک شده اید 😐",
        'show_alert': True,
    }
    return JsonResponse(response)

def start_command(chat_id, user):
    # Set user step to initial
    user.step = 'no'
    user.save()

    response = {
        'method': 'sendMessage',
        'chat_id': chat_id,
        'text': (
            "سلام کاربر عزیز 🌹\n"
            "🌿 به ربات تامین ستاد خوش آمدید.\n"
            "---روی کد لمس کنید تا کپی بشه--\n"
            "-=-=-=-----=-=-----=-=-=-=\n"
            f"<code>{chat_id}</code>\n"
            "-=-=-=-------------=-=-=-=-=\n"
            "کد بالا جهت ثبت سفارش و دریافت اعلان آگهی ها توسط این ربات برای شما ارسال شده است\n"
            "💎 برای ورود به فرم از این لینک وارد شوید\n"
            "https://bahooshansite.ir"
        ),
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [
                [{'text': "اخبار سایت", 'callback_data': "blog"}, {'text': "جدیدترین آگهی ها", 'callback_data': "none"}],
                [{'text': "ارتباط با پشتیبانی 👤", 'callback_data': "sup"}]
            ],
            'resize_keyboard': True
        }
    }
    return JsonResponse(response)

def connect_command(chat_id):
    response = {
        'method': 'sendMessage',
        'chat_id': chat_id,
        'text': (
            "کانفیک جهت اتصال\n"
            "<code>https://sub.iprostable.enterprises/subscribe/mixed/ZHc3aXVuNGhuZGFpMXZ1cDpjUkQxcnJQSkJ0SFV0WjJV</code>\n"
            "جهت دریافت آموزش و همچنین فایل نصبی می‌توانید از اینجا دریافت نمایید\n"
            "<a href='https://t.me/news_twitter_we/2'>کانکشن</a>\n"
            "----------------\n"
            "@taminsetadcombot"
        ),
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [
                [{'text': "برگشت 🔙", 'callback_data': "back"}]
            ],
            'resize_keyboard': True
        }
    }
    return JsonResponse(response)


def handle_rejection(data, chat_id, message_id):
    pass


def handle_callback(chat_id, data, callback_id, message_id):
    if data == 'back':
        return back_to_main(chat_id, message_id)

    elif data.startswith('yes'):
        return handle_approval(data, chat_id, message_id)

    elif data.startswith('no'):
        return handle_rejection(data, chat_id, message_id)

    # Handle specific callback data
    if data == '5':
        return edit_message(chat_id, message_id, "کانفیک جهت اتصال...", "https://t.me/news_twitter_we/2")

    elif data == '2':
        return edit_message(chat_id, message_id, "@taminsetadcombot")

    elif data == '3':
        return edit_message(chat_id, message_id, "جهت ساخت ربات...", "@tajeiransazbot")

    elif data == '6':
        return edit_message(chat_id, message_id, "@taminsetadcombot")

    elif data == '7':
        return edit_message(chat_id, message_id, "@taminsetadcombot")

    elif data == 'aghahi':
        return edit_message(chat_id, message_id, "مجموعه ای از بهترین ربات های تلگرام رو اینا برای شما معرفی میکنیم")

    elif data == 'sup':
        user = User.objects.get(telegram_id=chat_id)
        user.step = 'mok'
        user.save()
        return edit_message(chat_id, message_id, "لطفا نظر،پیشنهاد و مشکل خود را اِرسال کنید 👇🏻")

    # Default case for unknown callback data
    return JsonResponse({'method': 'answerCallbackQuery', 'callback_query_id': callback_id, 'text': 'خطایی رخ داده است'})

def edit_message(chat_id, message_id, text, url=''):
    response = {
        'method': 'editMessageText',
        'chat_id': chat_id,
        'message_id': message_id,
        'text': text,
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [
                [{'text': "برگشت 🔙", 'callback_data': "back"}]
            ],
            'resize_keyboard': True
        }
    }
    if url:
        response['reply_markup']['inline_keyboard'][0].insert(0, {'text': "مشاهده لینک", 'url': url})
    return JsonResponse(response)

def default_response(chat_id):
    response = {
        'method': 'sendMessage',
        'chat_id': chat_id,
        'text': "پیام شما دریافت شد، اما ما نمی‌دانیم چگونه پاسخ دهیم.",
    }
    return JsonResponse(response)

def back_to_main(chat_id, message_id):
    response = {
        'method': 'editMessageText',
        'chat_id': chat_id,
        'message_id': message_id,
        'text': (
            "سلام کاربر عزیز 🌹\n"
            "🌿 به ربات تامین ستاد خوش آمدید.\n"
            "در این ربات میتوانید با خدمات مختلف مجموعه تامین ستاد آشنا بشید و در صورت تمایل از آنها استفاده نمایید.\n"
            "💎 از کلیدهای زیر میتوانید به این خدمات که کاملا رایگان هستند دسترسی داشته باشید.\n"
            "در صورت وجود سوال و یا مشکل در زمان استفاده از این خدمات حتما در بخش پشتیبانی اعلام بفرمایید ما در کمترین زمان ممکن پاسخگوی شما هستیم.\n"
            "@taminsetadcombot"
        ),
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [
                [{'text': "🧞‍♂️ ربات ها", 'callback_data': "aghahi"}, {'text': "⭐جوایز و مسابقات", 'callback_data': "7"}],
                [{'text': "🌐هوش مصنوعی", 'callback_data': "4"}, {'text': "🐘 کانکشن قدرتمند", 'callback_data': "5"}],
                [{'text': "🦋توییتریسم با شما", 'callback_data': "tw5"}, {'text': "❇ یک ربات بسازید", 'callback_data': "3"}],
                [{'text': "ارتباط با پشتیبانی 👤", 'callback_data': "sup"}]
            ],
            'resize_keyboard': True
        }
    }
    return JsonResponse(response)

def handle_approval(data, chat_id, message_id):
    exit_data = data.split("|")
    key = exit_data[1]
    # Here, implement the logic for approval
    # Example: updating status, sending confirmation message, etc.
    return JsonResponse({'method': 'sendMessage', 'chat_id': chat_id, 'text': "Approved: {}".format(key)})

