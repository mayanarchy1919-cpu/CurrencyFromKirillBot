import time

import telebot
from extensions import RequestResponse, ConvertionException, currency
from config import config
from datetime import datetime

request_api = RequestResponse()

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Добро пожаловать! Этот бот поможет быстро конвертировать валюту по текущему курсу.\n\
Посмотреть доступные валюты: /values \n\
Чтобы воспользоваться введите команду в формате \n<название валюты> \
<в какую валюту перевести> \
<количество валюты>"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currency.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")

    if len(values) != 3:
        raise ConvertionException(f"Неверное количество параметров.")

    base, quote, amount = values

    if base == quote:
        raise ConvertionException(f"Конвертируемые валюты должны отличаться.")

    text = request_api.get_price(base, quote, amount)

    bot.send_message(message.chat.id, text)

while True:
    try:
        bot.polling(True, timeout=90)
    except Exception as e:
        print(datetime.now(), e)
        time.sleep(5)
        continue
