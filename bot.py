from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
from function import*

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('lets_go', lets_go)
main_handler = MessageHandler(Filters.text, main)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(main_handler)

print('server started')
updater.start_polling()
updater.idle()