from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton('Напиши имя своего персонажа')

mainmenu = ReplyKeyboardMarkup(resize_keyboard= True)
mainmenu.add(btnProfile)