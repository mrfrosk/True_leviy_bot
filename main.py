from data import token
import telebot
from Get_filtered_messages import get_filtered_messages

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["get"])
def handle_text(message):
    messages = [message for message in get_filtered_messages(message.text[5:]) if message != ""]
    if messages:
        for message in messages:
            bot.send_message(message.chat.id, message)
    else:
        bot.send_message(message.chat.id, "сообщений содержаших такую строку не было обнаружено")


@bot.message_handler(commands=["help"])
def bot_help(message):
    bot.send_message(message.chat.id, "чтобы  отфильтровать сообщения комманда /get пример:\n"
                                      "/get О кулаках")


bot.polling()
