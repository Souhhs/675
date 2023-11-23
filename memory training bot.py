from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import CallbackQuery
from telegram.ext import CallbackQueryHandler
TOKEN = '6122705534:AAFX-rebDVzmthirtedNB5Fz1QdsBAEE7jg'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_game(chat_id=update.effective_chat.id, game_short_name="memory")

start_handler = CommandHandler('start', start)

def button(update, context):
    user = update.effective_user
    query = update.callback_query
    query.answer(url='https://souhhs.github.io/nfgjfgl/', show_alert=False)

dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.add_handler(start_handler)
updater.start_polling()