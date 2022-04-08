import json
import logging
import requests

import db_connector as db

from settings import TOKEN
from settings import TG_API

from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    db.add_chat_id(chat_id)
    context.bot.send_message(chat_id=chat_id,
                             text="Hey !\n"
                                  "I'm a binance listening bot, "
                                  "if you want to subscribe or unsubscribe to the listening stream "
                                  "write /subscribe or /unsubscribe to me!")


def subscribe(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    db.add_sub(chat_id)
    context.bot.send_message(chat_id=chat_id, text="You subscribed to the stream !")


def unsubscribe(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    db.remove_sub(chat_id)
    context.bot.send_message(chat_id=chat_id, text="You unsubscribed to the stream !")


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")


def notify_all_subs(message: str) -> None:
    subs = db.get_subs()
    headers = {'Content-Type': 'application/json'}

    for chat_id in subs:
        if tg_chat_exists(chat_id):
            data_dict = {'chat_id': chat_id,
                         'text': message}
            data = json.dumps(data_dict)
            url = f'{TG_API}/sendMessage'
            response = requests.post(url,
                                     data=data,
                                     headers=headers,
                                     verify=True)


def tg_chat_exists(chat_id: str):
    data = {"chat_id": chat_id}
    r = requests.get(f"{TG_API}/getChat", params=data)
    d = r.json()
    if d["ok"]:
        return True
    elif not d["ok"] and d["error_code"] == 400:
        return False


def run_bot():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    sub_handler = CommandHandler('subscribe', subscribe)
    unsub_handler = CommandHandler('unsubscribe', unsubscribe)
    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(sub_handler)
    dispatcher.add_handler(unsub_handler)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
