def revers(num):
    if len(num) == 1:
        return num
    return num[-1] + revers(num[:-1])


user_num = input('Введите натуральное число: ')
print(revers(user_num))
