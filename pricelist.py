from actions import *


pricelist = []
while True:
    print("""
    1. Загрузка данных
    2. Поиск дешевых товаров
    3. Поиск товаров
    4. Добавление товара
    5. Выход
    """)
    x = int(input())
    if x == 1:
        filename = input("Введите имя файла ")
        pricelist = load(filename)
        print(f"{len(pricelist)} товаров загружено")
    elif x == 2:
        cheapest_goods = cheapest(pricelist)
        print_goods(cheapest_goods)
    elif x == 3:
        substring = input("Введите часть названия ")
        found = find(pricelist, substring)
        print_goods(found)
    elif x == 4:
        print('Введите ариткул, название и цену товара на отдельных строках')
        num, name, price = input(), input(), float(input())
        add(pricelist, num, name, price)
        print_goods(pricelist[-1:])
    elif x == 5:
        break
print("До свидания")
