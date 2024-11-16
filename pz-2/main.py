number = int(input("Введите двузначное число: "))

tens = number // 10
units = number % 10

print("Левая цифра (десятки):", tens)
print("Правая цифра (единицы):", units)
