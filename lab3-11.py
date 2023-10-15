# Число в степени
x = float(input("Введите число: "))
y = int(input("Введите степень: "))

output = 1
while y > 0:
    output *= x
    y -= 1

print(f"Вводимое число: {x} Вводимая степень: {y} Результат: {output}")