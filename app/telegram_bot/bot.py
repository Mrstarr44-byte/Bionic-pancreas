"""
app/telegram_bot/bot.py
Telegram bot — polling modunda bağımsız process olarak çalıştırılır.
Kullanım: python -m app.telegram_bot.bot
"""

import os
import logging

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


# ── Command Handlers ─────────────────────────────────────────────

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kullanıcıya hoş geldin mesajı gönderir."""
    await update.message.reply_text(
        "🩸 Biyonik Pankreas Bot'una hoş geldiniz!\n\n"
        "Bu bot, simülasyon sonuçlarınızı ve glukoz uyarılarınızı "
        "size anlık olarak iletir.\n\n"
        "Komutlar için /help yazabilirsiniz."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kullanılabilir komutları listeler."""
    text = (
        "📋 Kullanılabilir Komutlar:\n\n"
        "/start  — Hoş geldin mesajı\n"
        "/help   — Bu yardım menüsü\n"
        "/durum  — Bot'un aktif olduğunu doğrula"
    )
    await update.message.reply_text(text)


async def durum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot'un çalışıp çalışmadığını doğrular."""
    await update.message.reply_text("✅ Bot aktif ve çalışıyor!")


# ── Main ──────────────────────────────────────────────────────────

def main():
    """Botu polling modunda başlatır."""
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN ortam değişkeni tanımlı değil!")
        return

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("durum", durum_command))

    logger.info("Telegram bot polling modunda başlatılıyor…")
    application.run_polling()


if __name__ == "__main__":
    main()
