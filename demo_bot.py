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

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает главное меню"""
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("🛍️ Бот-магазин", callback_data="shop")],
        [InlineKeyboardButton("📢 Бот для канала", callback_data="channel")],
        [InlineKeyboardButton("📝 Бот-опросник", callback_data="survey")],
        [InlineKeyboardButton("💼 Заказать бота", callback_data="order")],
        [InlineKeyboardButton("📞 Контакты", callback_data="contacts")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "🎯 *Мое портфолио Telegram ботов*\n\nВыберите тип бота:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "shop":
        keyboard = [
            [InlineKeyboardButton("💼 Заказать такой же", callback_data="order")],
            [InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "🛍️ *Бот-магазин*\n\n"
            "Полнофункциональный магазин с:\n"
            "• Каталогом товаров\n"
            "• Корзиной покупок\n" 
            "• Кнопками оплаты\n"
            "• Управлением заказами\n"
            "• Админ-панелью\n\n"
            "💵 *Стоимость:* от 2,000₽\n"
            "⏱️ *Срок:* 3-5 дней",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    elif query.data == "channel":
        keyboard = [
            [InlineKeyboardButton("💼 Заказать такой же", callback_data="order")],
            [InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "📢 *Бот для канала*\n\n"
            "Автоматизация публикаций:\n"
            "• Автопостинг по расписанию\n"
            "• Управление контентом\n"
            "• Статистика канала\n"
            "• Планирование публикаций\n"
            "• Автоматический парсинг\n\n"
            "💵 *Стоимость:* от 1,500₽\n"
            "⏱️ *Срок:* 2-4 дня",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    elif query.data == "survey":
        keyboard = [
            [InlineKeyboardButton("💼 Заказать такой же", callback_data="order")],
            [InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "📝 *Бот-опросник*\n\n"
            "Сбор и анализ данных:\n"
            "• Создание опросов\n"
            "• Сбор ответов\n"
            "• Экспорт в CSV/Excel\n"
            "• Аналитика результатов\n"
            "• Автоматические отчеты\n\n"
            "💵 *Стоимость:* от 1,500₽\n"
            "⏱️ *Срок:* 2-3 дня",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    elif query.data == "order":
        keyboard = [
            [InlineKeyboardButton("🛍️ Бот-магазин", callback_data="shop")],
            [InlineKeyboardButton("📢 Бот для канала", callback_data="channel")],
            [InlineKeyboardButton("📝 Бот-опросник", callback_data="survey")],
            [InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "💼 *Заказать разработку бота*\n\n"
            "✅ *Что входит:*\n"
            "• Консультация и ТЗ\n"
            "• Разработка под ваши задачи\n"
            "• Тестирование и отладка\n"
            "• Установка на хостинг 24/7\n"
            "• Обучение использованию\n"
            "• Техподдержка 7 дней\n\n"
            "⏱️ *Сроки:* 2-5 дней\n"
            "💵 *Стоимость:* от 1,500₽\n\n"
            "📞 *Для заказа:*\n"
            "Telegram: @your_username\n"
            "Email: your@email.com\n\n"
            "Выберите тип бота или свяжитесь со мной:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    elif query.data == "contacts":
        keyboard = [
            [InlineKeyboardButton("💼 Заказать бота", callback_data="order")],
            [InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "📞 *Мои контакты:*\n\n"
            "💼 *Kwork:* your_kwork_link\n"
            "📱 *Telegram:* @your_username\n"
            "📧 *Email:* your@email.com\n"
            "💻 *GitHub:* github.com/yourusername\n\n"
            "🛠️ *Специализация:*\n"
            "• Telegram боты\n"
            "• Автоматизация бизнеса\n"
            "• Python разработка\n"
            "• Интеграция с API\n\n"
            "🚀 *Готов к сотрудничеству!*",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    elif query.data == "main_menu":
        await show_main_menu(update, context)

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
