from telegram import Update
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import ReplyKeyboardRemove
from config import bot_token
from events import show_events
#keyboard_buttons
CALLBACK_BUTTON1_REQ = "request nearest 5 deadlines"
CALLBACK_BUTTON4_MOODLE = 'open moodle'

def catch_err(f):
    def inner(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except Exception as e:
            print(f'Error {e}')
            raise e
    return inner


def main():
    updater = Updater(
        token = bot_token,
        use_context=True
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all,callback=message_handler))
    updater.start_polling()
    updater.idle()
@catch_err
def message_handler(update: Updater, context: CallbackContext):
    text = update.message.text 
    if text == CALLBACK_BUTTON1_REQ:
        return request_deadline_handler(update=update,context=CallbackContext)
    if text == CALLBACK_BUTTON4_MOODLE:
        return link_to_moodle_handler(update=update, context= CallbackContext)    
    reply_markup = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text=CALLBACK_BUTTON1_REQ)
            ],
            [
                KeyboardButton(text=CALLBACK_BUTTON4_MOODLE)
            ],
        ],
        resize_keyboard= True,
    )
    update.message.reply_text(
        text="Select any option",
        reply_markup = reply_markup,
    )
@catch_err
def request_deadline_handler(update: Updater, context: CallbackContext):
    update.message.reply_text(text=show_events()
    )
@catch_err
def link_to_moodle_handler(update: Updater, context: CallbackContext):
    update.message.reply_text(text='link to your moodle website')


if __name__ == '__main__':
    main()
