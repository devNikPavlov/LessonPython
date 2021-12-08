# Создание числовых списков

# функция range() - упрощает построение числовых последовательностей, здесь быдет вывод чисел от 1 до 4

for value in range(1, 5):
    print(value)

# Использование range() для создания числового списка
numbers = list(range(1, 6))
print(numbers)

# функция range() - также может пропускать числа в заданном диапазоне
# в этом примере функция начинает со значение 2, а затем увеличивает его на 2
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# с помощью функции range() - можно возвести в степень (**)
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)









