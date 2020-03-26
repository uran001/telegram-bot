from telegram.ext import Updater, CommandHandler
from googletrans import Translator
import requests
import re


def bop(bot, update):

	url = get_url()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)

def start_callback(context, update):
	translator = Translator()
	to_translate = " ".join(context.args)
	print(to_translate)
	translated = translator.translate(to_translate)
	chat_id = update.message.chat_id
	bot.send_text(chat_id=chat_id, text=translated)
	

def main():
	update = Updater('1015208196:AAEichyBYQerst24YHWMHlPclCR51AJALsU')
	dp = update.dispatcher
	dp.add_handler(CommandHandler('start', start_callback))
	update.start_polling()
	update.idle()

if __name__ == '__main__':
	main()