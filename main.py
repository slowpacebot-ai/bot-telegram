from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola 👋 Escribe: /placa ABC123")

async def placa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Consulta en prueba ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("placa", placa))
app.run_polling()
