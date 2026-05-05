import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBAPP_URL = "https://livinlavlin-svg.github.io/EnglishGrammar/"

KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("📅 Записаться на пробный урок", url="https://calendly.com/livinlavlin/30min")],
    [InlineKeyboardButton("💬 Только спросить", url="https://t.me/ohlavlin")],
    [InlineKeyboardButton("📢 Канал english.everyday", url="https://t.me/lavlin_english")],
    [InlineKeyboardButton("🎓 Открыть тренажёр", web_app=WebAppInfo(url=WEBAPP_URL))],
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! 👋 Выбери что тебя интересует:", reply_markup=KEYBOARD)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
