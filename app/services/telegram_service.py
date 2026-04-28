from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from app.config import TELEGRAM_TOKEN, ACCIONES
from app.services.market_data import get_data
from app.indicators.indicators import apply_indicators
from app.strategies.swing_strategy import generate_signal
from app.orchestrator.signal_dispatcher import dispatch_signal


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot activo")


async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Analizando mercado...")

    resultados = []

    for ticker in ACCIONES:
        df = get_data(ticker)

        if df is None or len(df) < 60:
            continue

        df = apply_indicators(df)
        signal = generate_signal(df)

        if signal:
            resultados.append((ticker, signal))

    if not resultados:
        await update.message.reply_text("❌ No hay señales")
        return

    mensaje = "📈 SEÑALES:\n\n"

    for t, s in resultados:
        mensaje += f"{t} | Precio: {round(s['precio'],2)} | RSI: {round(s['rsi'],2)}\n"

    await update.message.reply_text(mensaje)


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚙️ Ejecutando escaneo...")

    enviados = 0

    for ticker in ACCIONES:
        df = get_data(ticker)

        if df is None or len(df) < 60:
            continue

        df = apply_indicators(df)
        signal = generate_signal(df)

        if signal:
            dispatch_signal(ticker, signal)
            enviados += 1

    await update.message.reply_text(f"✅ {enviados} señales enviadas a n8n")


def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signals", signals))
    app.add_handler(CommandHandler("scan", scan))

    print("Bot corriendo...")
    app.run_polling()
