from telegram import Update, ForceReply, update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import APIKEY

# Get the dispatcher to register handlers

def merhaba(update: Update, context: CallbackContext):
    update.message.reply_text("Merhaba, daha emekleyen bir botum.");

updater = Updater(APIKEY)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("merhaba", merhaba))
updater.start_polling()
updater.idle()

