from config import token
import telebot
from Get_filtered_messages import get_filtered_messages

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["get"])
def handle_text(search_message):
    messages = [message for message in get_filtered_messages(search_message.text[5:]) if message != ""]
    if messages:
        for message in messages:
            bot.send_message(search_message.chat.id, message)
    else:
        bot.send_message(search_message.chat.id, "сообщений содержаших такую строку не было обнаружено")


@bot.message_handler(commands=["help"])
def bot_help(message):
    bot.send_message(message.chat.id, "что, отфильтровать посты комманда /get пример:\n"
                                      "/get Текст сообщения")


@bot.message_handler(commands=["test"])
def test_func(message):
    nameUsers = message.chat.id
    print(nameUsers)


bot.polling()
