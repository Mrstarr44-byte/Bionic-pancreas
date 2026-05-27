"""
app/telegram_bot/notifier.py
Flask uygulamasından çağrılabilen senkron Telegram bildirim fonksiyonları.

python-telegram-bot v21.x tamamen async'tir.
Flask senkron olduğu için asyncio.run() ile senkron wrapper kullanılır.
"""

import asyncio
import logging
import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def send_telegram_notification(message: str) -> bool:
    """
    Telegram'a mesaj gönderen senkron wrapper.

    Args:
        message: Gönderilecek metin.

    Returns:
        True ise başarılı, False ise hata veya eksik yapılandırma.
    """
    if not TOKEN or not CHAT_ID:
        logger.warning(
            "Telegram bildirimi gönderilemedi: "
            "TELEGRAM_BOT_TOKEN veya TELEGRAM_CHAT_ID tanımlı değil."
        )
        return False

    try:
        bot = Bot(token=TOKEN)
        asyncio.run(bot.send_message(chat_id=CHAT_ID, text=message))
        logger.info("Telegram bildirimi gönderildi.")
        return True
    except Exception as e:
        logger.error("Telegram bildirimi gönderilemedi: %s", e)
        return False


# ── Bildirim Türleri ──────────────────────────────────────────────

def send_hypo_alert(glucose: float) -> bool:
    """Hipoglisemi uyarısı gönderir (glukoz < 70)."""
    message = (
        "🥶 HİPOGLİSEMİ UYARISI!\n\n"
        f"Kan şekeri: {glucose} mg/dL\n"
        "Düşük kan şekeri tespit edildi.\n"
        "Lütfen hızlı karbonhidrat alınız."
    )
    return send_telegram_notification(message)


def send_hyper_alert(glucose: float) -> bool:
    """Hiperglisemi uyarısı gönderir (glukoz > 180)."""
    message = (
        "😓 HİPERGLİSEMİ UYARISI!\n\n"
        f"Kan şekeri: {glucose} mg/dL\n"
        "Yüksek kan şekeri tespit edildi.\n"
        "İnsülin dozu kontrol edilmelidir."
    )
    return send_telegram_notification(message)


def send_stable_message(glucose: float) -> bool:
    """Stabilite (normal aralık) mesajı gönderir."""
    message = (
        "😊 Kan Şekeri Stabil\n\n"
        f"Kan şekeri: {glucose} mg/dL\n"
        "Değerleriniz normal aralıkta. Harika!"
    )
    return send_telegram_notification(message)


def send_daily_summary(
    avg_glucose: float,
    min_glucose: float,
    max_glucose: float,
    sim_count: int
) -> bool:
    """Günlük özet raporu gönderir."""
    message = (
        "📊 Günlük Özet Raporu\n\n"
        f"Simülasyon sayısı: {sim_count}\n"
        f"Ortalama glukoz: {avg_glucose:.1f} mg/dL\n"
        f"Min glukoz: {min_glucose:.1f} mg/dL\n"
        f"Max glukoz: {max_glucose:.1f} mg/dL"
    )
    return send_telegram_notification(message)


def send_motivation() -> bool:
    """Motivasyon mesajı gönderir."""
    message = (
        "💪 Motivasyon Mesajı\n\n"
        "Sağlığınızı takip etmeye devam edin!\n"
        "Düzenli kontrol, sağlıklı yaşamın anahtarıdır. 🩸"
    )
    return send_telegram_notification(message)
