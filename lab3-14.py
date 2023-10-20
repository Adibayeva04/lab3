#программа, которая проверяет является ли введенное пользователем число простым числом

# Определяем функцию is_prime, которая проверяет, является ли число простым.
def is_prime(n):
    if n <= 1:
        return False  # Если число меньше или равно 1, оно не является простым.
    if n <= 3:
        return True   # Если число 2 или 3, оно простое.

    if n % 2 == 0 or n % 3 == 0:
        return False  # Если число четное или делится на 3, оно не является простым.

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Если число делится на i или i + 2, оно не является простым.
        i += 6

    return True  # Если число не подпадает под предыдущие условия, оно простое.

# Определяем функцию next_prime, которая находит следующее простое число после заданного числа num.
def next_prime(n):
    if n < 2:
        return 2
    next_n = n + 1
    while True:
        if is_prime(next_n):
            return next_n
        next_n += 1

# Начинаем бесконечный цикл для ввода и обработки данных.
while True:
    try:
        user_input = int(input("Введите число: "))
        if is_prime(user_input):
            print(f"{user_input} - простое число.")
        else:
            next_prime_n = next_prime(user_input)
            print(f"{user_input} - не простое число. Следующее простое число: {next_prime_n}")
    except ValueError:
        print("Введите корректное число.")

    continue_testing = input("Хотите продолжить тестирование? (да/нет): ")
    if continue_testing.lower() != "да":
        break  # Если пользователь не хочет продолжать тестирование, выходим из цикла.

