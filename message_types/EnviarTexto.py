
from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from dotenv import  dotenv_values
getenv = dotenv_values('.env')

TOKEN = getenv['TOKEN']

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    print(update.message.message_id)
    update.message.reply_text("<b>Hola</b> <i>Costumer</i>, <u>Quieres saber mas sobre nosotros?</u>, visita https://autopaquete.com", parse_mode=ParseMode.HTML)


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