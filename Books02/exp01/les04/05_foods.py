# копирование списка

my_foos = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foos[:]

print('My favorite foods are: ')
print(my_foos)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# копирование
my_foos.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are: ')
print(my_foos)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

