from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

 ←←← Pega aquí tu token
TOKEN = '8965082965:AAHFjMs7RADZn4Gc_3ZCck7dh8f1eORkbkE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Hola! Soy tu bot. ¿En qué te ayudo?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Comandos disponibles:\n/start - Iniciar\n/help - Esta ayuda')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Repite lo que el usuario dice
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers (comandos)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # Responder a cualquier mensaje de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()
