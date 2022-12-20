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

A = 0
B = 1

me_token = ""

bot = Bot(token=me_token)
updater = Updater(token=me_token)
dispatcher = updater.dispatcher

def run(update, context):
    context.bot.send_message(update.effective_chat.id,"Hello\n/help /run /filter_text")
    print("Hello\n/help /run /filter_text")

def filter_text(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите текст, и очистит все слова содержащие абв")
    print("Введите текст, и очистит все слова содержащие абв")
    return A

def filter2_text(update, context):
    text = update.message.text
    clear_text = filtf.filter_text(text)
    context.bot.send_message(update.effective_chat.id, f"Фильтрация завершена\n{clear_text}")
    print(f"{clear_text}\nФильтрация завершена")
    return ConversationHandler.END


def help(update, context):
    context.bot.send_message(update.effective_chat.id, "/help /run /filter_text")
    print("/help /run /filter_text")


def func(update, context): # 13.15
    text = update.message.text
    id = update.message.from_user.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    is_bot =  update.message.from_user.is_bot

    f = open("log.txt",'a+')
    f.write(f"{dt.datetime.now()}	{id}	{username}	{first_name}	{last_name}	{is_bot}\n{text}\n")
    f.close()

message_handler = MessageHandler(Filters.all, func)
filter_handled = CommandHandler("filter_text", filter_text)
# filter2_handled = CommandHandler("filter_text2", filter2_text)
start_handled = CommandHandler("run", run)
help_handler = CommandHandler("help",help)



conv_handler = ConversationHandler(entry_points=[start_handled],
                                   states={A: [filter2_text]})

# подключает к боту.
dispatcher.add_handler(start_handled)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(filter_handled)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()






# if __name__ == '__main__':
#     print("Запуск бота")
#     filter.run()
