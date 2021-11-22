from random import randint, uniform
a = input('Введите левую границу: ')
b = input('Введите правую границу: ')
# print(randint(int(a), int(b)))   # Случайное целое число
# print(uniform(float(a), float(b)))   # Случайное вещественное число
print(chr(randint(ord(a), ord(b))))   # Случайный символ
