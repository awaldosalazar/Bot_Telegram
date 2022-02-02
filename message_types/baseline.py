from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

from dotenv import  dotenv_values
getenv = dotenv_values('.env')

TOKEN = getenv['TOKEN']

print(TOKEN)

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    print(f'Id Costumer: [*{update.message.chat.id}*]  \nMessage Customer: [*{update.message.text}*]')
    update.message.reply_text(update.message.text)


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