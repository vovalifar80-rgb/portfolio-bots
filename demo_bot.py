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
    """Обработчик команды /start с кнопками"""
    keyboard = [
        [InlineKeyboardButton("🛍️ Бот-магазин", callback_data="shop")],
        [InlineKeyboardButton("📢 Бот для канала", callback_data="channel")],
        [InlineKeyboardButton("📝 Бот-опросник", callback_data="survey")],
        [InlineKeyboardButton("💼 Заказать бота", callback_data="order")],
        [InlineKeyboardButton("📞 Контакты", callback_data="contacts")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎯 *Добро пожаловать в мое портфолио!*\n\nВыберите тип бота:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "shop":
        await query.edit_message_text(
            "🛍️ *Бот-магазин*\n\n"
            "Полнофункциональный магазин с:\n"
            "• Каталогом товаров\n"
            "• Корзиной покупок\n" 
            "• Кнопками оплаты\n"
            "• Управлением заказами\n\n"
            "💵 Стоимость: от 2,000₽",
            parse_mode='Markdown'
        )
    elif query.data == "channel":
        await query.edit_message_text(
            "📢 *Бот для канала*\n\n"
            "Автоматизация публикаций:\n"
            "• Автопостинг по расписанию\n"
            "• Управление контентом\n"
            "• Статистика канала\n"
            "• Планирование публикаций\n\n"
            "💵 Стоимость: от 1,500₽",
            parse_mode='Markdown'
        )
    elif query.data == "survey":
        await query.edit_message_text(
            "📝 *Бот-опросник*\n\n"
            "Сбор и анализ данных:\n"
            "• Создание опросов\n"
            "• Сбор ответов\n"
            "• Экспорт в CSV\n"
            "• Аналитика результатов\n\n"
            "💵 Стоимость: от 1,500₽",
            parse_mode='Markdown'
        )
    elif query.data == "order":
        await query.edit_message_text(
            "💼 *Заказать разработку бота*\n\n"
            "📞 Telegram: @your_username\n"
            "📧 Email: your@email.com\n"
            "💻 Kwork: your_kwork_link\n\n"
            "✅ Бесплатная консультация\n"
            "✅ Срок: 2-5 дней\n"
            "✅ Техподдержка 7 дней",
            parse_mode='Markdown'
        )
    elif query.data == "contacts":
        await query.edit_message_text(
            "📞 *Мои контакты:*\n\n"
            "💼 Kwork: your_kwork_link\n"
            "📱 Telegram: @your_username\n"
            "📧 Email: your@email.com\n\n"
            "🚀 Готов к сотрудничеству!",
            parse_mode='Markdown'
        )

def main():
    if not BOT_TOKEN:
        logging.error("❌ BOT_TOKEN не установлен!")
        return
    
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_handler))
        
        logging.info("✅ Бот запущен и готов к работе!")
        application.run_polling()
        
    except Exception as e:
        logging.error(f"❌ Ошибка: {e}")

if __name__ == '__main__':
    main()
