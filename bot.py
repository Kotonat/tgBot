#библиотеки, которые загружаем из вне
import telebot
import logging
import os
import requests

TOKEN = '5571754006:AAGX0hNJh2vPbr0XSwryx24wqnjZl3RniXU'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Мой Git📟")
	item2 = types.KeyboardButton("Связь со мной📞")
	item3 = types.KeyboardButton("Рандомный кот🐱") #Третья кнопка

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Приветствую в своем боте, {0.first_name}! Актуальная информация по кнопкам 🤖".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Мой Git📟':
			bot.send_message(message.chat.id, 'https://github.com/Kotonat')
		elif message.text == 'Связь со мной📞':
			bot.send_message(message.chat.id, 'https://t.me/nat1894')
		elif message.text == 'Рандомный кот🐱':
			r = requests.get('https://api.thecatapi.com/v1/images/search')
			url = r.json()[0]['url']
			bot.send_photo(chat_id=message.chat.id, photo=url)
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)







#https://core.telegram.org/bots/api#available-methods