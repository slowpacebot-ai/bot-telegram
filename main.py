from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola 👋\nEscribe:\n/placa ABC123"
    )

async def placa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usa: /placa ABC123")
        return

    placa = context.args[0].upper()
    await update.message.reply_text(
        f"🚗 Placa: {placa}\nConsulta en prueba ✅"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("placa", placa))
    app.run_polling()

if __name__ == "__main__":
    main()
