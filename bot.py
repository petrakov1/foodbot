#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,ConversationHandler
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import redis
import json
import dataStorage
import dataAnal

TOKEN = "515081396:AAHw-n2i0iigt9iAPVhVgL5-p9ibiD3wd-0"

# FIRST, SECOND, HELP = range(3)

PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def allPlaces(bot, update):
    update.message.reply_text('Places')
    
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def button(bot, update):
    query = update.callback_query
    if query.data.find("like") != -1:
        array = str.replace(str(query.data),"like?","")
        list1 = array.split(',')
        place_id = int(list1[0])
        place = dataStorage.getPlace(place_id)
        dataStorage.changeUser(query.message.chat_id,place['tags'],0)
        bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                    message_id=update.callback_query.message.message_id,text="Выбор учтен 👌")
        
    elif query.data.find("location") != -1:
        array = str.replace(str(query.data),"location?","")
        list1 = array.split(',')
        place_id = int(list1[0])
        p = dataStorage.getPlace(place_id)
        bot.send_location(chat_id=query.message.chat_id,latitude=p['location']['lon'],longitude=p['location']['lat'])
    else:
        print(query.data)
def start(bot, update):
    update.message.reply_text('Отмечай ❤️ места которые тебе нравятся, и я буду учиться 💡')
    dataStorage.createUser(update.message.chat_id)

    location_keyboard = telegram.KeyboardButton(text="Найти где поесть", request_location=True)
    custom_keyboard = [[ location_keyboard ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id, 
                    text="Меню", 
                    reply_markup=reply_markup)
    places = dataStorage.getNPlaces(5)
    # print(places)
    for place in places:
        p = place
        button_list = [
        telegram.InlineKeyboardButton("❤️", callback_data="like?"+str(p['id'])),
        telegram.InlineKeyboardButton("Местоположение", callback_data="location?"+str(p['id']))]
        reply_markup = telegram.InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        # bot.send_photo(chat_id=update.message.chat_id, photo='http://phink.team/hotline/images/product/1/HQ/кроссовки-sf-air-force-1-mid-OnTrJDlm.png')
        bot.send_message(chat_id=update.message.chat_id,text='*'+p['name']+'*\n'+p['desc']+'\n \n'+p['address'],parse_mode=telegram.ParseMode.MARKDOWN,reply_markup=reply_markup)


def nearPlaces(bot,update):
    print("in")
    json_data = json.loads(dataStorage.getAllPlaces())
    user = json.loads(dataStorage.getUser(update.message.chat_id))
    places = dataAnal.getTopPlaces(json_data,user,(update.message.location.latitude,update.message.location.longitude))
    # print(places)
    for place in places:
        p = dataStorage.getPlace(place[0])
        button_list = [
        telegram.InlineKeyboardButton("❤️", callback_data="like?"+str(p['id'])),
        telegram.InlineKeyboardButton("Местоположение", callback_data="location?"+str(p['id']))]
        reply_markup = telegram.InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        # bot.send_photo(chat_id=update.message.chat_id, photo='http://phink.team/hotline/images/product/1/HQ/кроссовки-sf-air-force-1-mid-OnTrJDlm.png')
        bot.send_message(chat_id=update.message.chat_id,text='*'+p['name']+'*\n'+p['desc']+'\n \n'+p['address'],parse_mode=telegram.ParseMode.MARKDOWN,reply_markup=reply_markup)
    

def showPlace(bot,update):
    # print(dataStorage.getAllPlaces())
    places = dataStorage.getNPlaces(5)
    # print(places)
    for place in places:
        p = place
        button_list = [
        telegram.InlineKeyboardButton("❤️", callback_data="like?"+str(p['id'])),
        telegram.InlineKeyboardButton("Местоположение", callback_data="location?"+str(p['id']))]
        reply_markup = telegram.InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        # bot.send_photo(chat_id=update.message.chat_id, photo='http://phink.team/hotline/images/product/1/HQ/кроссовки-sf-air-force-1-mid-OnTrJDlm.png')
        bot.send_message(chat_id=update.message.chat_id,text='*'+p['name']+'*\n'+p['desc']+'\n \n'+p['address'],parse_mode=telegram.ParseMode.MARKDOWN,reply_markup=reply_markup)
    # update.message.reply_text(text='*Fenster Coffee*\ntest',parse_mode=telegram.ParseMode.MARKDOWN)
   

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def textHandlers(bot, update):
    bot.send_message(chat_id=update.message.chat_id,text='Like')
    update.message.reply_text(update.callback_query)


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
    dp.add_handler(CommandHandler("place", showPlace))

#     # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.location,nearPlaces))


#     # log all errors
    dp.add_error_handler(error)

    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('place', showPlace)],
    #     states={
    #         FIRST: [CallbackQueryHandler(textHandlers)]
    #     },
    #     fallbacks=[CommandHandler('start', start)]
    # )


    # updater.dispatcher.add_handler(conv_handler)

    updater.start_polling()

    # updater.start_webhook(listen="0.0.0.0",
                        # port=PORT,
                        # url_path=TOKEN)
    # updater.bot.set_webhook("https://spbfoodbot.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()

