from urllib import response

import requests
from requests.exceptions import RequestException

API_KEY = 'YOUR_TELEGRAM_API_KEY'  # Replace with your actual API key

def send_api_request(method, data=None):
    url = f"https://api.telegram.org/bot{API_KEY}/{method}"
    headers = {'Content-Type': 'application/json'}

    try:
        if data:
            response = requests.post(url, json=data, headers=headers)
        else:
            response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        return response.json()
    except RequestException as e:
        print(f"Error sending Telegram API request: {e}")
        return None

def send_message(chat_id, text, parse_mode='Markdown'):
    data = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode}
    return send_api_request('sendMessage', data)

def send_photo(chat_id, photo, caption=None):
    data = {'chat_id': chat_id, 'photo': photo}  # Assuming photo is a file-like object
    if caption:
        data['caption'] = caption
    return send_api_request('sendPhoto', data)

# Implement similar functions for other Telegram API methods (SendDocument, etc.)

def get_chat(chat_id):
    data = {'chat_id': chat_id}
    return send_api_request('getChat', data)

def get_me():
    return send_api_request('getMe')


