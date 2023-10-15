#программа, которая проверяет является ли введенное пользователем число простым числом

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(num):
    if num < 2:
        return 2
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

while True:
    try:
        user_input = int(input("Введите число: "))
        if is_prime(user_input):
            print(f"{user_input} - простое число.")
        else:
            next_prime_number = next_prime(user_input)
            print(f"{user_input} - не простое число. Следующее простое число: {next_prime_number}")
    except ValueError:
        print("Введите корректное число.")
    continue_testing = input("Хотите продолжить тестирование? (да/нет): ")
    if continue_testing.lower() != "да":
        break