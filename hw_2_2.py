num = input('Введите натуральное число: ')
even = 0
odd = 0
for _ in num:
    if int(_) % 2 == 0:
        even += 1
    elif int(_) % 2 != 0:
        odd += 1
print(f'В введенном натуральном числе {even} четных и {odd} нечетных цифр.')
