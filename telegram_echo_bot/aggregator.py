import telebot
from decouple import config

API_KEY = config('API_KEY_TG')
bot = telebot.TeleBot(API_KEY, parse_mode=None)


# @bot.message_handler(regexp="Total Wallet Value Per Account In BTC")
def handle_messages(messages):
    # bot.copy_message()
    for message in messages:
        # Do something with the message
        bot.reply_to(message, 'Hi')
        print(message)


print('Zuus Aggregator TS1 bot started....')
bot.set_update_listener(handle_messages)
bot.infinity_polling()
