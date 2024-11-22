#Даны два целых числа: A, B. Проверить истинность высказывания:
#"Числа A и B имеют одинаковую четность".
#Дано целое число, лежащее в диапазоне 1–999. Вывести его строку-описание вида:
#"четное двузначное число", "нечетное трехзначное число" и т. д.
def check_parity(a, b):
    try:
        return (a % 2 == b % 2)
    except TypeError:
        raise ValueError("Оба числа должны быть целыми")


def describe_number(n):
    try:
        if not (1 <= n <= 999):
            raise ValueError("Число должно быть в диапазоне от 1 до 999")
        parity = "четное" if n % 2 == 0 else "нечетное"
        if n < 10:
            digits = "однозначное"
        elif n < 100:
            digits = "двузначное"
        else:
            digits = "трехзначное"
        return f"{parity} {digits} число"
    except TypeError:
        raise ValueError("Число должно быть целым")


if __name__ == "__main__":
    try:
        # Ввод данных для проверки четности
        a = int(input("Введите первое целое число (A): "))
        b = int(input("Введите второе целое число (B): "))

        # Проверка четности
        if check_parity(a, b):
            print("Числа A и B имеют одинаковую четность.")
        else:
            print("Числа A и B имеют разную четность.")

        # Ввод данных для описания числа
        n = int(input("Введите число от 1 до 999: "))

        # Описание числа
        description = describe_number(n)
        print(f"Описание числа: {description}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
