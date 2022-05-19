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
    planet_text = update.message.text
    planetext = planet_text.split(' ')
    planet = planetext[1]
    print(planet)
    if planetext[1] == 'Mars' or planetext[1] == 'Марс':
        place = ephem.Mars('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Mercury':
        place = ephem.Mercury('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Venus':
        place = ephem.Venus('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con) 
    elif planetext[1] == 'Earth':
        place = ephem.Earth('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Jupiter':
        place = ephem.Jupiter('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Saturn':
        place = ephem.Saturn('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Uranus':
        place = ephem.Uranus('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Neptune':
        place = ephem.Neptune('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Pluto':
        place = ephem.Pluto('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
    elif planetext[1] == 'Sun':
        place = ephem.Sun('2022/05/19')
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1] == 'Moon':
        place = ephem.Moon('2022/05/19')
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
