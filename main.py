from decouple import config
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import requests
from bs4 import BeautifulSoup

TK = config('token')

async def hello(update: Update, context: CallbackContext):
    B_keys = [[KeyboardButton('استعلام 💰')],
              [KeyboardButton('جدید ترین شهر ها  🌐'), KeyboardButton('آخرین ارگان ها 📊')],
              [KeyboardButton('حساب کاریری ⭕')],
              [KeyboardButton('راهنما ℹ')],
              [KeyboardButton('پشتیبانی ☎'), KeyboardButton('جست و جوی آگهی 🔎')]]
    key_markup = ReplyKeyboardMarkup(
        keyboard=B_keys,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="یک گزینه را انتخاب کنید"
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'خوش آمدید {update.effective_user.first_name}',
        reply_markup=key_markup
    )

def get_price(url, css_selector):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.select_one(css_selector).text.strip()
    return price

async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if text == 'استعلام 💰':
        B_keys = [[KeyboardButton('دلار'), KeyboardButton('یوان')],
                  [KeyboardButton('یورو'), KeyboardButton('درهم')],
                  [KeyboardButton('لیر')]
                  ]
        key_markup = ReplyKeyboardMarkup(
            keyboard=B_keys,
            resize_keyboard=True,
            one_time_keyboard=True,
            input_field_placeholder="یک ارز را انتخاب کنید"
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='انتخاب کنید',
            reply_markup=key_markup
        )

    elif text in ['دلار', 'یوان', 'یورو', 'لیر','درهم']:
        urls_css_selectors = {
            'دلار': ("https://www.tgju.org/profile/price_dollar_rl", "#main > div.stocks-profile > div.stocks-header > div.stocks-header-main > div > div.fs-cell.fs-xl-3.fs-lg-3.fs-md-6.fs-sm-12.fs-xs-12.top-header-item-block-2.mobile-top-item-hide > div > h3.line.clearfix.mobile-hide-block > span.value > span:nth-child(1)"),
            'یورو': ("https://www.tgju.org/profile/price_eur", "#main > div.stocks-profile > div.stocks-header > div.stocks-header-main > div > div.fs-cell.fs-xl-3.fs-lg-3.fs-md-6.fs-sm-12.fs-xs-12.top-header-item-block-2.mobile-top-item-hide > div > h3.line.clearfix.mobile-hide-block > span.value > span:nth-child(1)"),
            'درهم': ("https://www.tgju.org/profile/price_aed", "#main > div.stocks-profile > div.stocks-header > div.stocks-header-main > div > div.fs-cell.fs-xl-3.fs-lg-3.fs-md-6.fs-sm-12.fs-xs-12.top-header-item-block-2.mobile-top-item-hide > div > h3.line.clearfix.mobile-hide-block > span.value > span:nth-child(1)"),
            'یوان': ("https://www.tgju.org/profile/price_cny", "#main > div.stocks-profile > div.stocks-header > div.stocks-header-main > div > div.fs-cell.fs-xl-3.fs-lg-3.fs-md-6.fs-sm-12.fs-xs-12.top-header-item-block-2.mobile-top-item-hide > div > h3.line.clearfix.mobile-hide-block > span.value > span:nth-child(1)"),
            'لیر': ("https://www.tgju.org/profile/price_try","#main > div.stocks-profile > div.stocks-header > div.stocks-header-main > div > div.fs-cell.fs-xl-3.fs-lg-3.fs-md-6.fs-sm-12.fs-xs-12.top-header-item-block-2.mobile-top-item-hide > div > h3.line.clearfix.mobile-hide-block > span.value > span:nth-child(1)")
        }

        url, css_selector = urls_css_selectors.get(text, (None, None))
        if url and css_selector:
            try:
                price = get_price(url, css_selector)
                await update.message.reply_text(f"قیمت فعلی {text} : {price}")
            except Exception as e:
                await update.message.reply_text("خطا در واکشی قیمت. لطفاً بعداً دوباره امتحان کنید.")
        else:
            await update.message.reply_text("Currency not supported.")

def main():
    app = Application.builder().token(TK).build()
    app.add_handler(CommandHandler('start', hello))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()
