import telebot
import requests
import json
from config import config

bot = telebot.TeleBot(config.BOT_TOKEN)

keys = {'Dollars': 'USD',
        'Euro': 'EUR',
        'Rubles': 'RUB'}

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
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(" ")
    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}")
    total_base = json.loads(r.content)[keys[base]]
    text = f"Стоимость {amount} {quote} в {base} равна {float(amount) * float(total_base)}"
    bot.send_message(message.chat.id, text)
bot.polling()