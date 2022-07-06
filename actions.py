def load(filename):
    """
        Загрузка данных
    """
    import csv
    pricelist = []
    with open(filename) as csvfile:
            reader = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
            del reader[0]
            pricelist = [(num, name, float(price.replace(',', '.')))
                         for num, name, price in reader]
    return pricelist


def find(pricelist, substring):
    """
        Поиск товаров по подстроке
    """
    return [x for x in pricelist if substring.lower() in x[1].lower()]


def cheapest(pricelist, count=5):
    """
        Поиск 5 самых дешёвых товаров 
    """
    a = pricelist[:]  # копия прайслиста
    ## a[j][0] - num,  a[j][2] - price
    for i in range(count):  # count элементов
        for j in range(len(a) - 2, i - 1, -1):
            if a[j + 1][2] < a[j][2] or (
                    a[j + 1][2] == a[j][2] and a[j + 1][0] < a[j][0]):
                a[j], a[j + 1] = a[j + 1], a[j]
        return a[:count]  # возвращаем срез - count элементов


def print_goods(pricelist):
    """
        Модифицированный print 
    """
    if pricelist != []:
        for s in pricelist:
            print(*s)
    return


def add(pricelist, num, name, price):
    """
        Добавление товара 
    """
    pricelist.append((num, name, price))


if __name__ == '__main__':  # проверка, что модуль запущен как программа
    print("Actions is loaded")
    pricelist = [(121, "Спички", 4.50),
                 (124, "Соль", 12.20),
                 (126, "Хлеб", 28.30),
                 (154, "Кефир", 34.10),
                 (165, "Молоко", 54.30)
                 ]
    print_goods(pricelist)
