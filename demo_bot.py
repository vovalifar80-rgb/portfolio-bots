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

# Список твоих ботов для портфолио
PORTFOLIO_BOTS = {
    'shop': {
        'name': '??? Бот-магазин',
        'username': '@PortfolioShopDemo_bot',
        'description': 'Полнофункциональный магазин с каталогом товаров, корзиной и кнопками оплаты',
        'features': ['Каталог товаров', 'Корзина покупок', 'Инлайн-кнопки', 'Управление заказами']
    },
    'channel': {
        'name': '?? Бот для канала', 
        'username': '@PortfolioChannelBot',
        'description': 'Автоматизация публикаций в Telegram каналах',
        'features': ['Автопостинг', 'Расписание', 'Статистика', 'Управление контентом']
    },
    'survey': {
        'name': '?? Бот-опросник',
        'username': '@PortfolioSurveyBot', 
        'description': 'Сбор и анализ данных через опросы',
        'features': ['Создание опросов', 'Сбор ответов', 'Экспорт в CSV', 'Аналитика']
    },
    'game': {
        'name': '?? Игровой бот',
        'username': '@PortfolioGameBot',
        'description': 'Развлекательный бот с мини-играми и рейтингами',
        'features': ['Мини-игры', 'Рейтинг игроков', 'Таблица лидеров', 'Мультиплеер']
    }
}

def start(update: Update, context: CallbackContext):
    """Главное меню портфолио"""
    keyboard = [
        [InlineKeyboardButton("??? Бот-магазин", callback_data="bot_shop")],
        [InlineKeyboardButton("?? Бот для канала", callback_data="bot_channel")],
        [InlineKeyboardButton("?? Бот-опросник", callback_data="bot_survey")],
        [InlineKeyboardButton("?? Игровой бот", callback_data="bot_game")],
        [InlineKeyboardButton("?? Заказать бота", callback_data="order")],
        [InlineKeyboardButton("?? Контакты", callback_data="contacts")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = """
?? *Добро пожаловать в мое портфолио!*

Я разработчик Telegram ботов. Здесь вы можете посмотреть примеры моих работ и заказать собственного бота.

*Что я делаю:*
 Боты для бизнеса и автоматизации
 Игровые и развлекательные боты  
 Боты для каналов и групп
 Интеграция с API и базами данных

Выберите бота для демонстрации:
"""
    update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

def show_bot_details(update: Update, context: CallbackContext, bot_key):
    """Показывает детали конкретного бота"""
    query = update.callback_query
    bot_data = PORTFOLIO_BOTS[bot_key]
    
    features_text = "\n".join([f" {feature}" for feature in bot_data['features']])
    
    description = f"""
*{bot_data['name']}*

?? *Описание:* {bot_data['description']}

? *Возможности:*
{features_text}

?? *Username:* {bot_data['username']}

*Технологии:* Python, python-telegram-bot, Render
"""
    
    keyboard = [
        [InlineKeyboardButton("?? Назад к портфолио", callback_data="back_to_portfolio")],
        [InlineKeyboardButton("?? Заказать похожего", callback_data="order")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(description, reply_markup=reply_markup, parse_mode='Markdown')

def button_handler(update: Update, context: CallbackContext):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    data = query.data
    
    if data == "back_to_portfolio":
        # Возврат к главному меню
        keyboard = [
            [InlineKeyboardButton("??? Бот-магазин", callback_data="bot_shop")],
            [InlineKeyboardButton("?? Бот для канала", callback_data="bot_channel")],
            [InlineKeyboardButton("?? Бот-опросник", callback_data="bot_survey")],
            [InlineKeyboardButton("?? Игровой бот", callback_data="bot_game")],
            [InlineKeyboardButton("?? Заказать бота", callback_data="order")],
            [InlineKeyboardButton("?? Контакты", callback_data="contacts")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        query.edit_message_text(
            "?? *Мое портфолио Telegram ботов*\n\nВыберите бота для демонстрации:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif data.startswith("bot_"):
        bot_key = data.split("_")[1]
        show_bot_details(update, context, bot_key)
    
    elif data == "order":
        order_text = """
?? *Заказать разработку бота*

*Что входит в услугу:*
? Консультация и обсуждение ТЗ
? Разработка бота под ваши задачи
? Тестирование и отладка
? Установка на хостинг 24/7
? Обучение использованию
? Техподдержка 7 дней

*Сроки:* 2-5 дней в зависимости от сложности

*Стоимость:* от 1,500?

?? *Для заказа:* @your_username
?? *Email:* your.email@mail.ru

*Или найдите меня на Kwork:*
[Ваша ссылка на Kwork]
"""
        keyboard = [[InlineKeyboardButton("?? Назад", callback_data="back_to_portfolio")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        query.edit_message_text(order_text, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif data == "contacts":
        contacts_text = """
?? *Мои контакты:*

?? *Kwork:* [Ваша ссылка на Kwork]
?? *Telegram:* @your_username
?? *Email:* your.email@mail.ru
?? *GitHub:* github.com/yourusername

*Работаю над:*
 Telegram ботами
 Автоматизацией бизнеса
 Python разработкой

*Готов к сотрудничеству!* ??
"""
        keyboard = [[InlineKeyboardButton("?? Назад", callback_data="back_to_portfolio")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        query.edit_message_text(contacts_text, reply_markup=reply_markup, parse_mode='Markdown')

def main():
    """Основная функция"""
    if not BOT_TOKEN:
        logging.error("? BOT_TOKEN не установлен!")
        return
    
    try:
        updater = Updater(BOT_TOKEN, use_context=True)
        
        # Добавляем обработчики
        updater.dispatcher.add_handler(CommandHandler("start", start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
        
        logging.info("?? Демо-бот портфолио запущен!")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logging.error(f"? Ошибка при запуске: {e}")

if __name__ == '__main__':
    main()