#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import logging

from setup import PROXY, TOKEN
from telegram import Bot, Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

ACTION_COUNT = 0

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def log(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        update = args[0]
        if update and hasattr(update, "warning"):
            with open(f"{update.message.chat.id}.txt", "a") as handle:
                print(func, file=handle)
        if update and hasattr(update, "message") and hasattr(update, "effective_user"):
            global ACTION_COUNT
            ACTION_COUNT += 1
            if ACTION_COUNT > 5:
                f = open(f"{update.message.chat.id}.txt").readlines()
                for i in range(5):
                    f.pop(0)
                with open(f"{update.message.chat.id}.txt", "w") as F:
                    F.writelines(f)
            with open (f"{update.message.chat.id}.txt", "a") as handle:
                print(f"Действие {ACTION_COUNT}:", file=handle)
                print(f"user: {update.effective_user.first_name}", file=handle)
                print(f"function: {func.__name__}", file=handle)
                print(f"message: {update.message.text}\n", file=handle)
    return inner

@log
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'Привет, {update.effective_user.first_name}!')
    f = open(f"{update.message.chat.id}.txt", "w+")

@log
def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Введи команду /start для начала. ')

@log
def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

@log
def history(update: Update, context: CallbackContext):
    """Display 5 latest ACTION_HISTORY elements when the command /history is issued."""
    handle = open(f"{update.message.chat.id}.txt", "r")
    update.message.reply_text("Последние 5 действий:")
    update.message.reply_text(handle.read())
    handle.close()

@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')


def main():
    bot = Bot(
        token="895548858:AAHWTesxKmd6rpC3P4u6QJejsordITl3cYU",
        base_url=PROXY,  # delete it if connection via VPN
    )
    updater = Updater(bot=bot, use_context=True)

    # on different commands - answer in Telegram
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', chat_help))
    updater.dispatcher.add_handler(CommandHandler('history', history))

    # on noncommand i.e message - echo the message on Telegram
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.info('Start Bot')
    main()
