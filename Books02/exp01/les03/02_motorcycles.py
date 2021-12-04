# Изменение, добавление и удаление элементов

# Изменение элементов в списке

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Добавление элементов в список

# Присоединение элементов в конце списка - метод append()
motorcycles2 = ['honda',
                'yamaha',
                'suzuki']
print(motorcycles2)

motorcycles2.append('ducati')
print(motorcycles2)

# Например, мы можем начать с пустого списка и добавлять в него элементы
motorcycles3 = []

motorcycles3.append('honda')
motorcycles3.append('yamaha')
motorcycles3.append('suzuki')

print(motorcycles3)

# Вставка элементов в список
motorcycles3.insert(0, 'ducati')
print(motorcycles3)

# Удаление элементов из списка

# Лдаление элементов с использованием команды - del
print(motorcycles3)
del motorcycles3[3]
print(motorcycles3)

# Удаление элемента с использованием метода pop() - этот метод удаляет последний элемент из писка, но
# позволяет работать с ним после удаления.
print(motorcycles3)

popped_motorcycle = motorcycles3.pop()
print(motorcycles3)
print(popped_motorcycle)

# Извлечение элементов из произвольной позиции списка
# метод pop() - может использоваться для удаления элементов в произвольной позиции списка
motorcycles4 = ['honda', 'yamaha', 'suzuki']
print(motorcycles4)

first_owned = motorcycles4.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

# Простое правило поможет определиться: если собираетесь просто удалить элемент из списка, никак не используя
# его, выбирайте команду del; если же вы намерены использовать элемент после удаления из списка, выбирайте -
# метод pop()

# Удаление элементов по значению
# Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение элемента, используйте
# метод remove()
motorcycles5 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles5)

motorcycles5.remove('ducati')
print(motorcycles5)

# 'honda' - сохраняется в переменной с именем too_expensive, затем эта переменная сообщает Python, какое
# значение должно быть удалено из списка. Далее значчение 'honda' было удалено из списка, но продолжает
# храниться в переменной too_expensive

too_expensive = 'honda'
motorcycles5.remove(too_expensive)
print(motorcycles5)
print(f'\nA {too_expensive.title()} is too expensive for me.')
















