

import random

def print_forty_symbols():

    symbols = ''.join(random.choices('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', k=40))
    print(f"Сгенерированные символы: {symbols}")

def sort_inc3(a, b, c):

    return tuple(sorted([a, b, c]))

def main():
    try:
        # Задача 1: Вывод сорока случайных символов
        print("Задача 1: Вывод сорока случайных символов")
        print_forty_symbols()

        # Задача 2: Сортировка двух наборов из трёх чисел
        print("\nЗадача 2: Сортировка чисел")

        # Первый набор чисел
        a1, b1, c1 = 3.5, 1.2, 4.8
        print(f"Исходный набор 1: A1 = {a1}, B1 = {b1}, C1 = {c1}")
        a1, b1, c1 = sort_inc3(a1, b1, c1)
        print(f"Отсортированный набор 1: A1 = {a1}, B1 = {b1}, C1 = {c1}")

        # Второй набор чисел
        a2, b2, c2 = 7.4, 2.1, 5.3
        print(f"\nИсходный набор 2: A2 = {a2}, B2 = {b2}, C2 = {c2}")
        a2, b2, c2 = sort_inc3(a2, b2, c2)
        print(f"Отсортированный набор 2: A2 = {a2}, B2 = {b2}, C2 = {c2}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
