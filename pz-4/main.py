#1. Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).
#2. Дано целое число N (> 1). Найти наименьшее целое число K, при котором
#выполняется неравенство 3К > N
def calculate_product(n):
    try:
        if n <= 0:
            raise ValueError("Число N должно быть больше 0.")
        product = 1.0
        for i in range(1, n + 1):
            product *= (1 + i / 10.0)
        return product
    except Exception as e:
        return f"Ошибка: {e}"


def find_min_k(n):
    try:
        if n <= 1:
            raise ValueError("Число N должно быть больше 1.")
        k = 0
        while 3**k <= n:
            k += 1
        return k
    except Exception as e:
        return f"Ошибка: {e}"


if __name__ == "__main__":
    try:
        # Пользовательский ввод для первой задачи
        N1 = int(input("Введите значение N для задачи 1 (N > 0): "))
        result_task1 = calculate_product(N1)
        print(f"Произведение {N1} множителей: {result_task1}")

        # Пользовательский ввод для второй задачи
        N2 = int(input("Введите значение N для задачи 2 (N > 1): "))
        result_task2 = find_min_k(N2)
        print(f"Наименьшее K, при котором 3^K > {N2}: {result_task2}")

    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
