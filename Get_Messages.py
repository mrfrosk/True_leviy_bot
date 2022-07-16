from asyncio import set_event_loop, new_event_loop

from data import api_id, api_hash, app_name
from telethon.sync import TelegramClient

def get_messages(search_message):
    messages = []
    set_event_loop(new_event_loop())
    with TelegramClient(app_name, api_id, api_hash) as client:
        search_message = str(search_message.text).split("get ")[1]
        for message in client.iter_messages("Пруфы Жожеков"):
            try:
                if search_message in message.text:
                    messages.append(message.text)
            except TypeError:
                continue

    return messages if messages else ["среди сообщение не того, что вы ввели"]
