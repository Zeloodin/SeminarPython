#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Знакомство с языком Python (семинары)
# Урок 9. Возможна ли жизнь без PIP?
# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# 2) Создайте Бота для игры с конфетами человек против бота. (Дополнительно)

import time, datetime as dt
import filter_func as filtf
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

me_token = "5833295241:AAH2JQWPBuLpox3-WdaXSSpx96vpMCvzLYU"

bot = Bot(token=me_token)
updater = Updater(token=me_token)
dispatcher = updater.dispatcher

def run(update, context):
    print("command: run")
    context.bot.send_message(update.effective_chat.id,"Hello\n/help /filter /filter_text")
    print("Hello\n/help /filter /filter_text")

def filter_text(update, context):
    print("command: filter")
    text = update.message.text
    clear_text = filtf.filter(text)
    context.bot.send_message(update.effective_chat.id, clear_text)

def help(update, context):
    print("command: help")
    context.bot.send_message(update.effective_chat.id, "/help /filter /filter_text")
    print("/help /filter /filter_text")


def func(update, context):
    text = update.message.text
    id = update.message.from_user.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    is_bot =  update.message.from_user.is_bot

    f = open("log.txt",'a+')
    f.write(f"{dt.datetime.now()}	{id}	{username}	{first_name}	{last_name}	{is_bot}\n{text}\n")
    f.close()

run_handled = CommandHandler("run", run)
start_handled = CommandHandler("start", run) # иногда работает и или с задержкой.
filter_handled = CommandHandler("filter_text", filter_text)
filter2_handled = CommandHandler("filter", filter_text) # иногда работает и или с задержкой.
help_handled = CommandHandler("help", help)
message_handler = MessageHandler(Filters.all, func)


dispatcher.add_handler(message_handler)
dispatcher.add_handler(help_handled)
dispatcher.add_handler(filter_handled)
dispatcher.add_handler(filter2_handled)
dispatcher.add_handler(start_handled)
dispatcher.add_handler(run_handled)

updater.start_polling()
updater.idle()






# if __name__ == '__main__':
#     print("Запуск бота")
#     filter.run()
