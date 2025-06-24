from pathlib import Path
import re

# Шаблон: строка целиком = 4 цифры [–диапазон]? + «год» или «гг.»
heading_pattern = re.compile(r'^\s*\d{4}(?:–\d{4})?\s*(?:год|гг\.)\s*$')
target_heading = '1857 год'

# Пути относительно скрипта
script_dir  = Path(__file__).parent
input_path  = script_dir / 'Dostoevsky.txt'
output_path = script_dir / 'Dostoevsky_1857.txt'

capturing = False
buffer = []

with input_path.open(encoding='utf-8') as fin:
    for raw in fin:
        line = raw.rstrip('\n')
        if not capturing:
            # Ждём начала блока
            if line.strip() == target_heading:
                capturing = True
                buffer.append(raw)           # сохраняем строку-заголовок
        else:
            # Если встретили новый заголовок-лет (и это не наш 1857) — выходим
            if heading_pattern.match(line) and line.strip() != target_heading:
                break
            buffer.append(raw)

# Записываем только собранный блок
with output_path.open('w', encoding='utf-8') as fout:
    fout.writelines(buffer)

print(f'Блок «{target_heading}» сохранён в файл:\n  {output_path}')
