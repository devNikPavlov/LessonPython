# Перебор всего списка

magicians = ['alice', 'david', 'carolina']

# определяется цикл for. Эта строка приказывает Python взять очередное имя из списка и сохранить его в
# переменной magician
for magician in magicians:
    print(magician)


# Более сложные действия в циклах for
magicians2 = ['alice', 'david', 'carolina']
for magician2 in magicians2:
    print(f'{magician2.title()}, that was a great trick!')

    print(f"I can't wait to see your next trick, {magician2.title()}.\n")

# Выполнение действий после цикла for
print('Thank you, everyone. That was a great magic show!')


