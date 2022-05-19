"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    #Посчитать и вывести суммарное количество продаж для каждого товара
    def sum_sales(items_sold):
      sold_sum_product = 0
      for solds1 in items_sold:
        sold_sum_product = sold_sum_product + solds1 
      return sold_sum_product

    for product in phones:
      sold_sum = sum_sales(product['items_sold'])
      product['sold_sum'] = sold_sum
      print(f'Sold sum {product["product"]} : {product["sold_sum"]}')

    #Посчитать и вывести среднее количество продаж для каждого товара. 
    #На самом деле этот кусок кода можно было не писать и просто вставить строку принт в цикл выше, 
    #но тогда это было бы не точное выполнение задачи, т.к. по условиям надо сначала вывести все суммы, а уже потом средние
    for product_avg in phones:
      sold_sum = sum_sales(product_avg['items_sold'])
      product_avg['sold_sum_avg'] = sold_sum/len(product_avg['items_sold'])
      print(f'Sold avg_sum {product_avg["product"]} : {round(product_avg["sold_sum_avg"],1)}')

    #Посчитать и вывести суммарное количество продаж всех товаров
    sum_all = 0
    for phone in phones:
      sum_all = sum_all + phone['sold_sum']
    print(f'Суммарные продажи всех смартфонов: {sum_all}')

    #Посчитать и вывести среднее количество продаж всех товаров

    avg_all = 0
    for phone_avg in phones:
      avg_all = avg_all + phone_avg['sold_sum_avg']
    print(f'Средние продажи всех смартфонов: {round(avg_all/len(phones), 1)}')


    
      
    
if __name__ == "__main__":
    main()
