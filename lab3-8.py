#программа которая пропускает четные числа и выводит сумму всех нечетных
sum_odd = 0
n = int(input("Введите число: "))
if n % 2 == 0:
    continue
else:
    sum_odd += n
    print("Сумма нечетных",sum_odd)