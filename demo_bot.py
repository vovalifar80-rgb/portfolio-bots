import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("BOT-MAGAZIN", callback_data="shop")],
        [InlineKeyboardButton("BOT-DLYA-KANALA", callback_data="channel")],
        [InlineKeyboardButton("ZAKAZAT", callback_data="order")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('PORTFOLIO BOT!', reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Rabotaet!")

def main():
    if not BOT_TOKEN:
        logging.error("NO BOT_TOKEN!")
        return
    
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_handler))
        
        logging.info("=== BOT STARTED ===")
        application.run_polling()
        
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    main()
