# -*- coding: utf-8 -*-
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv('BOT_TOKEN')

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("BOT-MAGAZIN", callback_data="shop")],
        [InlineKeyboardButton("BOT-DLYA-KANALA", callback_data="channel")],
        [InlineKeyboardButton("ZAKAZAT", callback_data="order")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('PORTFOLIO BOT!', reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text("Rabotaet!")

def main():
    if not BOT_TOKEN:
        logging.error("NO BOT_TOKEN!")
        return
    
    updater = Updater(BOT_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
    
    logging.info("=== BOT STARTED ===")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
