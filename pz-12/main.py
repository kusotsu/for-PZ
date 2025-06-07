import string


def analyze_numbers(nums):
    """
    Принимает список целых чисел и возвращает кортеж:
      (min_positive, list_div5, avg_div5)
    Если положительных нет, min_positive = None.
    Если нет чисел, кратных 5, list_div5 = [], avg_div5 = None.
    """
    # Генератор положительных чисел
    positives = (x for x in nums if x > 0)
    # Вычислим минимум среди положительных
    try:
        min_positive = min(positives)
    except ValueError:
        min_positive = None

    # Список элементов, кратных 5
    div5 = [x for x in nums if x % 5 == 0]
    avg_div5 = sum(div5) / len(div5) if div5 else None

    return min_positive, div5, avg_div5


def extract_punctuation(s):
    """
    Возвращает строку, содержащую только символы пунктуации из s.
    """
    return ''.join(ch for ch in s if ch in string.punctuation)


def main():
    # --- Часть 1: анализ чисел ---
    nums = [12, -5, 0, 25, 7, 30, -15, 5, 3]

    print("Исходная последовательность:", nums)
    min_pos, multiples_of_5, avg5 = analyze_numbers(nums)

    if min_pos is not None:
        print("1) Минимальный среди положительных:", min_pos)
    else:
        print("1) Положительных элементов нет.")

    print("2) Элементы, кратные 5:", multiples_of_5)
    if avg5 is not None:
        print(f"3) Среднее арифметическое кратных 5: {avg5:.2f}")
    else:
        print("3) Нет элементов, кратных 5.")

    # --- Часть 2: извлечение пунктуации ---
    template = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol})}msg"'
    print("\nИсходная строка:")
    print(template)
    punctuation_only = extract_punctuation(template)
    print("Только знаки пунктуации:")
    print(punctuation_only)


if __name__ == "__main__":
    main()