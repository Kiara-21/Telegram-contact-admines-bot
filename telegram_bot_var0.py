#May Omnissiah forgive me my sins and bless this code. Amen.

import telegram.ext
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler

Token = "INSERT YOUR TOKEN HERE"

updater = telegram.ext.Updater("INSERT YOUR TOKEN HERE", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Вітаю, надішліть ваше повідомлення і я його передам адмінам")

def echo(update, context):
    context.bot.forward_message(chat_id='INSERT YOUR GROUP ID HERE', from_chat_id=update.message.chat_id, message_id=update.message.message_id)

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.all, echo))

updater.start_polling()
updater.idle()
