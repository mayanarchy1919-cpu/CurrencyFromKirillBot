import telebot
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


bot.polling()