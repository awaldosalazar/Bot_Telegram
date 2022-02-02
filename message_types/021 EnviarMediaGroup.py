
from telegram import Update, ParseMode, InputMediaPhoto, InputMediaVideo
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import time

TOKEN = ""
RUTA = "E:\\ProyectosPersonales\\Udemy\\TelegramBot\\Grabaciones\\data\\"

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    
    inputPhoto = InputMediaPhoto(open(RUTA+"bateria.jpg", "rb"))
    inputVideo = InputMediaVideo(open(RUTA+"movie.mp4", "rb"))

    update.message.reply_media_group([inputPhoto, inputVideo])

        



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