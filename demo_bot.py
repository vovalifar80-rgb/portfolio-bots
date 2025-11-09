# -*- coding: utf-8 -*-
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Список ботов для портфолио
PORTFOLIO_BOTS = {
    'shop': {
        'name': 'BOT-MAGAZIN',
        'username': '@PortfolioShopDemo_bot',
        'description': 'Polnofunkcionalnyj magazin s katalogom tovarov',
        'features': ['Katalog tovarov', 'Korzina pokupok', 'Knopki oplaty']
    },
    'channel': {
        'name': 'BOT DLJA KANALA', 
        'username': '@PortfolioChannelBot',
        'description': 'Avtomatizacija publikacij v Telegram kanalah',
        'features': ['Avtoposting', 'Raspisanie', 'Statistika']
    }
}

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("BOT-MAGAZIN", callback_data="bot_shop")],
        [InlineKeyboardButton("BOT DLJA KANALA", callback_data="bot_channel")],
        [InlineKeyboardButton("ZAKAZAT BOTA", callback_data="order")],
        [InlineKeyboardButton("KONTAKTY", callback_data="contacts")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = "Dobro pozhalovat v moe portfolio! Vyberite bota:"
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

def show_bot_details(update: Update, context: CallbackContext, bot_key):
    query = update.callback_query
    bot_data = PORTFOLIO_BOTS[bot_key]
    
    features_text = "\n".join([f"- {feature}" for feature in bot_data['features']])
    
    description = f"{bot_data['name']}\n\nOpisanie: {bot_data['description']}\n\nVozmozhnosti:\n{features_text}\n\nUsername: {bot_data['username']}"
    
    keyboard = [
        [InlineKeyboardButton("NAZAD", callback_data="back_to_portfolio")],
        [InlineKeyboardButton("ZAKAZAT", callback_data="order")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(description, reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    
    if data == "back_to_portfolio":
        keyboard = [
            [InlineKeyboardButton("BOT-MAGAZIN", callback_data="bot_shop")],
            [InlineKeyboardButton("BOT DLJA KANALA", callback_data="bot_channel")],
            [InlineKeyboardButton("ZAKAZAT BOTA", callback_data="order")],
            [InlineKeyboardButton("KONTAKTY", callback_data="contacts")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Moe portfolio botov:", reply_markup=reply_markup)
    
    elif data.startswith("bot_"):
        bot_key = data.split("_")[1]
        show_bot_details(update, context, bot_key)
    
    elif data == "order":
        order_text = "Zakazat razrabotku bota:\n\nTelegram: @your_username\nEmail: your@email.com\nKwork: your_kwork_link"
        keyboard = [[InlineKeyboardButton("NAZAD", callback_data="back_to_portfolio")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(order_text, reply_markup=reply_markup)
    
    elif data == "contacts":
        contacts_text = "Kontakty:\n\nTelegram: @your_username\nEmail: your@email.com\nKwork: your_kwork_link"
        keyboard = [[InlineKeyboardButton("NAZAD", callback_data="back_to_portfolio")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(contacts_text, reply_markup=reply_markup)

def main():
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN ne ustanovlen!")
        return
    
    try:
        updater = Updater(BOT_TOKEN, use_context=True)
        updater.dispatcher.add_handler(CommandHandler("start", start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
        
        logging.info("Demo-bot zapuschen!")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logging.error(f"Oshibka pri zapuske: {e}")

if __name__ == '__main__':
    main()
