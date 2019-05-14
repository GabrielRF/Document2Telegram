import inotify.adapters
import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')
FOLDER = os.getenv('FOLDER', '/tmp/')
EXTENSION = os.getenv('EXTENSION', '')
DESTINATION = os.getenv('DESTINATION')

notifier = inotify.adapters.InotifyTree(FOLDER)
bot = telebot.TeleBot(TOKEN)

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CLOSE_WRITE' in event[1] and EXTENSION in event[3]:
            file_path = event[2] + '/' + event[3]
            file_open = open(file_path, 'rb')
            bot.send_chat_action(DESTINATION, 'upload_document')
            bot.send_document(DESTINATION, file_open)

