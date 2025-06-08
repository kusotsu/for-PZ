"""
В двумерном списке найти сумму и произведение элементов строки N (N задать с
клавиатуры).
2. В двумерном списке найти сумму элементов второй половины матрицы
"""


import math


def input_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Считывает матрицу размером rows×cols с клавиатуры.
    """
    matrix = []
    print(f"Введите {rows} строк по {cols} чисел, разделённых пробелом:")
    for i in range(rows):
        while True:
            row = input(f"Строка {i + 1}: ").split()
            if len(row) != cols:
                print(f"Ожидалось {cols} чисел, попробуйте ещё раз.")
                continue
            try:
                matrix.append([int(x) for x in row])
                break
            except ValueError:
                print("Ошибка: вводимые элементы должны быть целыми числами.")
    return matrix


def sum_and_product_of_row(matrix: list[list[int]], n: int) -> tuple[int, int]:
    """
    Возвращает (сумму, произведение) элементов строки с индексом n.
    """
    row = matrix[n]
    total = sum(row)
    product = math.prod(row)
    return total, product


def sum_of_second_half(matrix: list[list[int]]) -> int:
    """
    Возвращает сумму элементов второй половины матрицы по строкам.
    Если число строк нечётно, в "половину" попадёт больше строк:
    например, при 5 строках вторая половина — строки с индексами 2,3,4.
    """
    rows = len(matrix)
    start = rows // 2
    # генератор пробегает по всем элементам строк второй половины
    return sum(
        element
        for row in matrix[start:]
        for element in row
    )


def main():
    m = int(input("Введите число строк матрицы (m): "))
    n = int(input("Введите число столбцов матрицы (n): "))

    mat = input_matrix(m, n)

    print("\nИсходная матрица:")
    for row in mat:
        print(*row)

    k = int(input("\nВведите номер строки N (1–{}): ".format(m)))
    if not (1 <= k <= m):
        print("Неверный номер строки. Выход.")
        return
    idx = k - 1

    s, p = sum_and_product_of_row(mat, idx)
    print(f"\nЗадача 1:\nСумма элементов строки {k}: {s}\nПроизведение элементов строки {k}: {p}")

    sum_half = sum_of_second_half(mat)
    print(f"\nЗадача 2:\nСумма элементов второй половины матрицы: {sum_half}")


if __name__ == "__main__":
    main()
