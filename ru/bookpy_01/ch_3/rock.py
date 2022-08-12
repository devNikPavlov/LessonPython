#TODO random, if-elif-else,

# генерирование случайного числа
# сначала нужно импортировать библиотеку и объявляем переменную winner
import random

winner = ''

# сначала указываем имя модуля, затем ставим разделительную точку, далее указываем имя функции
# random.randint(0, 2)

# компьютер делает произвольный выбор, генерируя случайное целое число в диапазоне от 0 до 2,
# а затем сопостовляя его с соответствующей строкой
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'камень'
elif random_choice == 1:
    computer_choice = 'бумага'
else:
    computer_choice = 'ножницы'

# С помощью функции input() запрашиваем выбор пользователя
user_choice = input('камень, ножницы, бумага?')

# если компьютер и человек сделали одинаковый выбор, то ничья
if computer_choice == user_choice:
    winner = 'Ничья'
# здесь реализована логика игры: мы опредеяем победителя и соответствующим образом меняем переменную winner
elif computer_choice == 'бумага' and user_choice == 'камень':
    winner = 'Компьютер'
elif computer_choice == 'камень' and user_choice == 'ножницы':
    winner = 'Компьютер'
elif computer_choice == 'ножницы' and user_choice == 'бумага':
    winner = 'Компьютер'
else:
    winner = 'Пользователь'

# здесь мы объявляем либо ничью, либо победителя и сообщаем о выборе компьютера
if winner == 'Ничья':
    print('Мы оба выбрали', computer_choice + ', играем снова.')
else:
    print(winner, 'выиграл, я выбрал', computer_choice + '.')








