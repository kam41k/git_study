def row_sum(n):
    if n == 1:
        return 1
    elif n % 2 != 0:
        return 1/(2**(n-1)) + row_sum(n-1)
    elif n % 2 == 0:
        return -1/(2**(n-1)) + row_sum(n-1)


user_n = int(input('Введите число n: '))
print(row_sum(user_n))
