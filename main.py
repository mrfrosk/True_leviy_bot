import asyncio

from data import token
import telebot
from Get_Messages import get_messages

bot = telebot.TeleBot(token)



@bot.message_handler(commands=["get"])
def handle_text(message):
    for i in get_messages(message):
        try:
            bot.send_message(message.chat.id, i)
        except telebot.apihelper.ApiTelegramException:
            continue


@bot.message_handler(commands=["help"])
def bot_help(message):
    bot.send_message(message.chat.id, "что,s отфильтровать посты комманда /get: пример\n"
                                      "/get О кулаках")
bot.polling()
