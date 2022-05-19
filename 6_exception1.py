"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    
    while True:
      try:
        user_say = input('Как дела? ')
        if user_say.lower() == 'хорошо': #Но это не точное выполнение ТЗ, т.к. в ТЗ Хорошо только с большой буквы, но я сделал так
            break
        else:
            'ничего не делаем'
      except (KeyboardInterrupt):
        print('Пока!')
        break
        
        

    
if __name__ == "__main__":
    hello_user()
    
