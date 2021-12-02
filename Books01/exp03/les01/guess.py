#TODO - import, модули, randint(), for, str(), int(), float(), if & break

# Это игра по угадыванию чисел

"""
Хотя Python включает в себя множество встроенных функций, некоторые функции написаны в отдельных программах,
называемых Модулями. Вы можете использовать эти функции, импортируя соответствующие модули в вашу программу с помощью
инструкции import
"""

# Это инструкция import. Инструкция - это предписание, которое выполняет какое-либо действие, но не вычисляет значение,
# как это делает выражение
import random

guessesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

"""
импортируется модуль random, в нем находится функция randint() - эта функция будет генерировать случайное число 
"""
number = random.randint(1, 20)
print('Что ж, '  + myName + ', я загадываю число от 1 до 20.')

"""
Циклы позволяют выполнять кода несколько раз, например for
"""
for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number + '.')

"""
Преобразование значений при помощи функции int(), float(), str()

Инструкция if
"""










