import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import redis

TOKEN = "515081396:AAHw-n2i0iigt9iAPVhVgL5-p9ibiD3wd-0"

PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def allPlaces(bot, update):
    update.message.reply_text('Places')
    




# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
#     # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

#     # Get the dispatcher to register handlers
    dp = updater.dispatcher

#     # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("allplaces", allPlaces))

#     # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

#     # log all errors
    dp.add_error_handler(error)


    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TOKEN)
    updater.bot.set_webhook("https://spbfoodbot.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()

