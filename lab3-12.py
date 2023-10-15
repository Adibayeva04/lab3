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

try:
    N = int(input("Введите число: "))
    if N <= 0:
        print("Введите положительное число: ")
    else:
        print(f"Простые числа в промежутке 1 to {N}:")
        n = 2
        while n <= N:
            if is_prime(n):
                print(n, end=" ")
            n += 1
except ValueError:
    print("Ввод неверный")