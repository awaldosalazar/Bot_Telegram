
from telegram import Update, ParseMode, Poll
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import time

TOKEN = ""

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_document(open("E:\\ProyectosPersonales\\Udemy\\TelegramBot\\Grabaciones\\data\\prueba.pdf", "rb"), caption="Mi primer PDF", 
        thumb=open("E:\\ProyectosPersonales\\Udemy\\TelegramBot\\Grabaciones\\data\\taller.jpg", "rb"))

        



def main() -> None:
    """Start the bot."""
    # Creamos Updater y le pasamos el token
    updater = Updater(TOKEN)

    # Obtenemos el dispatcher para registrar los handlers
    dispatcher = updater.dispatcher

    # Handler para eco
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Iniciar el bot
    updater.start_polling()

    #Mantener el proceso hasta que se pulse Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()