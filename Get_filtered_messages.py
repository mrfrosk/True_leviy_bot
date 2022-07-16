from asyncio import set_event_loop, new_event_loop

from data import api_id, api_hash, app_name, channel_name
from telethon.sync import TelegramClient


def get_filtered_messages(search_message):
    messages = []
    set_event_loop(new_event_loop())
    with TelegramClient(app_name, api_id, api_hash) as client:
        for message in client.iter_messages(channel_name):
            if isinstance(message.text, str) and search_message in message.text:
                messages.append(message.text)
    return messages
