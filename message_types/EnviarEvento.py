
from telegram import Update, ParseMode, ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from dotenv import  dotenv_values

getenv = dotenv_values('.env')

TOKEN = getenv['TOKEN']

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    lat, lon = 20.67010722556849, -103.41222198910394
    update.message.reply_venue(lat, lon, title = "Autopaquete", 
        address="La mejor solucion para tu neogocio", google_place_id="ChIJIxI7v4WuKIQR47wheuA8H7Q", google_place_type="storage")



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