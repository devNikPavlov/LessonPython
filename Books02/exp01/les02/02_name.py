# Строки
# в строках могут быть как - одинарные, так и двойные кавычки

message = 'Это язык Python'
message2 = "Это тоже язык Python"
message3 = "д'Артаньян"
message4 = 'это фирма "Python"'

print(message)
print(message2)
print(message3)
print(message4)

print()

# Изменение регистра символов в строках

# В этом примере в переменной name сохраняется строка, состоящая из букв нижнего регистра. За именем переменной
# в команде print() следует вызов метода title(). Метод title() - преобразует первый символ слова в строке в верхний
# регистр
name = 'ada lovelace'
print(name.title())

# метод lower() - особенно полезен для хранения данных, а upper() - приводит все слова в нижний регистр
name2 = 'ADA LOVELACE'
print(name2.upper())
print(name2.lower())













