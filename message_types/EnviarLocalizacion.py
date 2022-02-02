
from telegram import Update, ParseMode, ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import time
from dotenv import  dotenv_values

getenv = dotenv_values('.env')

TOKEN = getenv['TOKEN']

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    lat, lon = 20.67010722556849, -103.41222198910394
    first_location_message = update.message.reply_location(lat, lon, live_period=60)
    for i in range(10):
        time.sleep(5)
        lat += 0.00005
        lon += 0.00005
        first_location_message.edit_live_location(lat, lon)
    update.message.reply_location(lat, lon)



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