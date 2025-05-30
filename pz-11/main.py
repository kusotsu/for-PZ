"""
Вариант 11.

1) Сгенерировать текстовый файл data.txt с последовательностью из целых
   положительных и отрицательных чисел. Затем сформировать файл report.txt
   с отчётом:
     Исходные данные: <список чисел>
     Количество элементов: <n>
     Минимальный элемент: <min>
     Количество положительных элементов в первой половине: <count>

2) Из файла text18-11.txt вывести на экран его содержимое и количество
   знаков препинания. Затем в файл shortest.txt записать строку минимальной
   длины из этого файла.
"""

import random
import string
import sys
from pathlib import Path

HERE = Path(__file__).parent.resolve()


def generate_numbers_file(
    filename: Path, count: int, low: int = -100, high: int = 100
) -> list[int]:
    """
    Генерирует файл filename со случайными целыми числами в диапазоне [low, high].
    Возвращает список сгенерированных чисел.
    """
    numbers = [random.randint(low, high) for _ in range(count)]
    try:
        with filename.open('w', encoding='utf-8') as f:
            f.write(' '.join(str(x) for x in numbers))
    except IOError as e:
        print(f"Ошибка записи в файл {filename}: {e}", file=sys.stderr)
        sys.exit(1)
    return numbers


def create_report(
    src_numbers: list[int], report_filename: Path
) -> None:
    """
    По списку src_numbers создаёт отчёт report_filename в требуемом формате.
    """
    n = len(src_numbers)
    minimum = min(src_numbers) if src_numbers else None
    half = src_numbers[: n // 2]
    positives_first_half = sum(1 for x in half if x > 0)

    lines = [
        f"Исходные данные: {' '.join(str(x) for x in src_numbers)}",
        f"Количество элементов: {n}",
        f"Минимальный элемент: {minimum}",
        f"Количество положительных элементов в первой половине: {positives_first_half}",
    ]

    try:
        with report_filename.open('w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    except IOError as e:
        print(f"Ошибка записи в файл {report_filename}: {e}", file=sys.stderr)
        sys.exit(1)


def analyze_text_file(
    src_filename: Path, output_filename: Path
) -> None:
    """
    Читает src_filename, печатает его содержимое и количество знаков препинания.
    Записывает в output_filename строку минимальной длины из этого файла.
    """
    for enc in ('utf-16', 'utf-8-sig'):
        try:
            text = src_filename.read_text(encoding=enc)
            print(f"Файл '{src_filename.name}' прочитан в кодировке {enc}")
            break
        except (UnicodeError, IOError):
            continue
    else:
        try:
            text = src_filename.read_text(encoding='utf-8', errors='replace')
            print(f"Файл '{src_filename.name}' прочитан в utf-8 с errors='replace'")
        except IOError as e:
            print(f"Ошибка чтения файла {src_filename}: {e}", file=sys.stderr)
            sys.exit(1)

    print("\nСодержимое файла:")
    print(text)

    punct = set(string.punctuation + '—«»…')
    count_punct = sum(1 for ch in text if ch in punct)
    print(f"\nКоличество знаков препинания: {count_punct}")

    lines = text.splitlines()
    if not lines:
        print(f"Файл {src_filename.name} пуст, нечего записывать.")
        return

    shortest = min(lines, key=len)
    try:
        with output_filename.open('w', encoding='utf-8') as f:
            f.write(shortest)
        print(f"\nКороткая строка ({len(shortest)} символов) записана в {output_filename.name}")
    except IOError as e:
        print(f"Ошибка записи в файл {output_filename}: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    # --- Пункт 1: генерация чисел и отчёт ---
    try:
        count = int(input("Введите количество чисел для генерации: "))
    except ValueError:
        print("Нужно ввести целое число.", file=sys.stderr)
        sys.exit(1)

    data_txt = HERE / 'data.txt'
    report_txt = HERE / 'report.txt'
    numbers = generate_numbers_file(data_txt, count)
    create_report(numbers, report_txt)
    print(f"Файлы '{data_txt.name}' и '{report_txt.name}' успешно созданы.")

    # --- Пункт 2: анализ text18-11.txt ---
    src = HERE / 'text18-11.txt'      
    shortest_txt = HERE / 'shortest.txt'
    analyze_text_file(src, shortest_txt)


if __name__ == '__main__':
    main()
