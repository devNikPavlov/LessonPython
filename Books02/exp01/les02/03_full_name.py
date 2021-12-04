# Использование переменных в строках

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

# Такие строки называются f-строками. Буква f происходит от слова "format" и форматирует в строку. f-строки
# появились в python3.6
# Например, сложная строка
print(f'Hello, {full_name.title()}!')

# можно и так, сохранить в переменной
message2 = f'Hello, {full_name.title()}!'
print(message2)

# Табуляции - комбинация символов (\t) и разрывы строк - (\n)
print('Python')
print('\tPython')

print('Языки: \nPython \nC \nJavaScript')
print('Языки: \n\tPython \n\tC \n\tJavaScript')

# Удаление пропусков. Лишние пропуски могут вызывать путаницу в программах. Типичный пример - проверка имени
# пользователя при входе на сайт
# у правого края
name = ' python '
name = name.rstrip()    # сначало пропуск удаляется с правого края, затем записывается в переменную

# у левого края
name = name.lstrip()

# с обоих концов
name = name.strip()
















