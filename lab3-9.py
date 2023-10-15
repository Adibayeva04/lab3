#рандомные числа
import random

# Создает случайное число от 1 до 100
rndm = random.randint(1, 100)

while True:
    try:
        num = int(input("Угадай число: "))

        if num == rndm:
            print("Вы угадали число! :", rndm)
#завершить игру если пользователь угадал
            break
        elif num < rndm:
            print("Слишком маленькое")
        else:
            print("Слишком большое")

    except ValueError:
        print("Ввод данных неверный")