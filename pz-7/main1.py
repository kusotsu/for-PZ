#2. Дана строка, содержащая полное имя файла. Выделить из этой строки название
#первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
#вывести символ «\».

def first_directory(a: str) -> str:
    parts = a.split("\\")
    if len(parts) > 1 and parts[0] == "":
        return parts[1]
    return "\\"


a = input("Введите полное имя файла: ")
print("Результат:", first_directory(a))
