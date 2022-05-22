"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
import ephem
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет!')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def eph(update, context):
    date_today = date.today()
    planet_text = update.message.text
    planetext = planet_text.split(' ')
    planet = planetext[1]
    print(planet)
    if planetext[1] == 'mars'.lower() or planetext[1] == 'марс'.lower():
        place = ephem.Mars(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'mercury'.lower():
        place = ephem.Mercury(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'venus'.lower():
        place = ephem.Venus(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con) 
    elif planetext[1] == 'earth'.lower():
        place = ephem.Earth(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'jupiter'.lower():
        place = ephem.Jupiter(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'saturn'.lower():
        place = ephem.Saturn(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'uranus'.lower():
        place = ephem.Uranus(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'neptune'.lower():
        place = ephem.Neptune(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'pluto'.lower():
        place = ephem.Pluto(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
    elif planetext[1] == 'sun'.lower():
        place = ephem.Sun(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'moon'.lower():
        place = ephem.Moon(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    
          
    else:
        update.message.reply_text('Такой планеты в солнечной системе нет')
   
  


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", eph))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
