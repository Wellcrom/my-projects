import random
import time
# проверить введено ли число, а не буква!!!
def nask():
    print('Введите целое количество чисел для сортировки в диапазоне от 20 до 1000')
    while type:
        getNumber = input()
        try:
            getTempNumber = float(getNumber)
        except ValueError:
                print('"' + getNumber + '"' + ' - не является числом! Повторите ввод числа!')
        else:
            n = float(getTempNumber)
            amin = 20
            amax = 1000
            int_check = (n).is_integer() # проверка числа на целостность
            if int_check == True:
                if n < amin:
                    print('Введённое число меньше минимально возможного, повторите ввод числа!')
                    return nask()
                elif n > amax:
                    print('Введённое число больше максимально возможного, повторите ввод числа!')
                    return nask()
                else:
                    return n
            else:
                print('Введённое число не целое, повторите ввод числа!')
                return nask()


def bub_sort(n,m): # n - int(checked_n), m - spisok
    start_time = time.process_time()
    for i in range(n - 1):
        for j in range(n - 2, i - 1, -1):
            if m[j + 1] < m[j]:
                m[j], m[j + 1] = m[j + 1], m[j]
    #print(*m) # убрать 
    finish_time = time.process_time()
    print(f"Количество чисел в списке: {n}")
    print(f"Процессорное время, которое было затрачено на сортировку: {(finish_time - start_time):.{3}f}c")
    first_10min = [x for x in m[0:10]]
    sum_first = sum(first_10min)
    print(f"Сумма 10 минимальных чисел отсортированного списка: {sum_first}")
    last_10max = [x for x in m[(len(m) - 10):len(m)]]
    sum_last = sum(last_10max)
    print(f"Сумма 10 максимальных чисел отсортированного списка: {sum_last}")

checked_n = nask()
#print(checked_n) # убрать
#print(int(checked_n)) # убрать 
spisok = []
for i in range(int(checked_n)):
    spisok.append(random.randint(10000, 99999))
#print(spisok) № убрать
            
bub_sort(int(checked_n),spisok)