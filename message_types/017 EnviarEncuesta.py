
from telegram import Update, ParseMode, Poll
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import time

TOKEN = ""

# Handlers
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_poll("¿Te gusta el curso?", ["Si", "No"], is_anonymous=False, allows_multiple_answers=True, type = Poll.QUIZ, 
        correct_option_id=0, explanation="Respuesta correcta: Si, ya que me he esforzado bastante! jaja", open_period=100)



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