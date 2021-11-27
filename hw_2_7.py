n = input('Введите любое натуральное число: ')
if n.isdigit() and int(n) > 0:
    n = int(n)
    check_sum = 0
    for i in range(1, n + 1):
        check_sum += i
    check_multi = n * (n + 1) / 2
    print('Равенство 1+2+..+n = n*(n+1)/2 - выполняется.') if check_sum == check_multi \
        else print('Равенство 1+2+..+n = n*(n+1)/2 -  не выполняется.')
elif not n.isdigit() or int(n) < 1:
    print('Вы ввели не натуральное число.')
