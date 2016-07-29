#!/usr/bin/python3
# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

TOKEN = 'SEU TOKEN VEM AQUI'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher                                    

def start(bot, update):      
    bot.sendMessage(chat_id=update.message.chat_id, text="Este é o bot da discórdia")

start_handler = CommandHandler('start', start)                   
dispatcher.add_handler(start_handler)                                                              

def bobo(bot, update):
    nome=update.message.from_user.name
    texto="Eu acho que " + nome  + " é bobo"
    bot.sendMessage(chat_id=update.message.chat_id, text=texto)       

bobo_handler = CommandHandler('bobo', bobo)
dispatcher.add_handler(bobo_handler)

def discordo(bot, update):
    nome=update.message.from_user.username
    if nome=='INSIRA NOME DO USUARIO SEM ARROBA':
        bot.sendMessage(chat_id=update.message.chat_id, text="Eu discordo do(a) @"+ nome +"!")

discordo_handler = MessageHandler([Filters.text],discordo)
dispatcher.add_handler(discordo_handler)

updater.start_polling()