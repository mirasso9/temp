# madeline/madeline_installer.py

import os
import sys
import requests
import logging
from telethon import TelegramClient, events

# تنظیم لاگ‌گیری
logging.basicConfig(level=logging.INFO)

# ثابت‌ها
RELEASE_TEMPLATE = 'https://phar.madelineproto.xyz/release{version}?v=new'
PHAR_TEMPLATE = 'https://github.com/danog/MadelineProto/releases/latest/download/madeline{version}.phar?v={release}'

# تابع برای دانلود و بررسی فایل PHAR
def download_phar(version, remote_release):
    url = PHAR_TEMPLATE.format(version=version, release=remote_release)
    response = requests.get(url)
    if response.status_code == 200:
        phar_path = os.path.join(os.getcwd(), f"madeline-{remote_release}.phar")
        with open(phar_path, 'wb') as f:
            f.write(response.content)
        return phar_path
    logging.error('Failed to download the PHAR file')
    return None

# بررسی نسخه پایتون
if sys.version_info < (3, 9):
    raise RuntimeError("MadelineProto requires at least Python 3.9.")

# منطق اصلی
def install_madeline():
    version = str(min(81, sys.version_info.major * 10 + sys.version_info.minor))
    release_url = RELEASE_TEMPLATE.format(version=version)
    response = requests.get(release_url)
    if response.status_code == 200:
        remote_release = response.text.strip()
        logging.info(f"Latest release: {remote_release}")
        phar_path = download_phar(version, remote_release)
        if phar_path:
            logging.info(f"Downloaded PHAR file: {phar_path}")
            # شبیه‌سازی بارگذاری فایل PHAR
            # در پایتون، شما کتابخانه را مستقیماً وارد و استفاده می‌کنید
        else:
            logging.error('Failed to download PHAR file')
    else:
        logging.error('Failed to fetch release information')

# اجرای نصب
install_madeline()
