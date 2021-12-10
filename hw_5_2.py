first_num = list(input('Введите первое шестнадцатиричное число: '))
second_num = list(input('Введите второе шестнадцатиричное число: '))
summa = list(hex(int(''.join(first_num), base=16) + int(''.join(second_num), base=16)).upper())[2:]
multi = list(hex(int(''.join(first_num), base=16) * int(''.join(second_num), base=16)).upper())[2:]
print(f'Сумма чисел  {"".join(summa)}, произведение  {"".join(multi)}')
