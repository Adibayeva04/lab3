# обратное число
n_1 = int(input("Введите целое число: "))

# Последнюю цифру первого числа переносим во второе
n_3 = n_1 % 10
n_2 = n_3

# Избавляемся от последней цифры первого числа
n_1 = n_1 // 10

while n_1 > 0:
    # находим остаток - последнюю цифру
    n_3 = n_1 % 10
    # делим нацело - удаляем последнюю цифру
    n_1 = n_1 // 10
    # увеличиваем разрядность второго числа
    n_2 = n_2 * 10
    # добавляем очередную цифру
    n_2 = n_2 + n_3

print('"Обратное" ему число:', n_2)