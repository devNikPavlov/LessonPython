#TODO random

# генерирование случайного числа
# сначала нужно импортировать библиотеку
import random

# сначала указываем имя модуля, затем ставим разделительную точку, далее указываем имя функции
# random.randint(0, 2)
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'камень'
elif random_choice == 1:
    computer_choice = 'бумага'
else:
    computer_choice = 'ножницы'

print('Компьютер выбирает', computer_choice)

