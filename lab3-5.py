#найти сумму цифр числа
n = input("Введите число: ")
sum = 0
#используем цикл for чтобы определить есть ли в строке цифры и вывести их сумму
for val in n:
    if val.isdigit():
        sum += int(val)
        print(f"Сумма цифр в данной строке : {sum}")