from memory_profiler import profile


@profile(precision=7)
def prime_num_for(i):
    if i < 3:
        return i+1
    k = 2
    num = 3
    while k < i:
        num += 1
        prime = True
        for div in range(2, num):
            if num % div == 0:
                prime = False
                break
        if prime:
            k += 1
    del k
    del i
    print(num)


@profile(precision=7)
def prime_eratos(i):
    length = i*15
    num_list = [num for num in range(length)]
    num_list[1] = 0
    for prime in num_list:
        if prime:
            for num in range(prime**2, length, prime):
                num_list[num] = 0
    num_list = sorted(list(set(num_list)))
    del length
    print(num_list[i])


@profile(precision=7)
def hw_3_4():
    from random import randint
    rand_list = [randint(50, 100) for _ in range(100)]
    rand_set = list(set(rand_list))
    max_cnt = 0
    num_max_cnt = 0
    for item in rand_set:
        if rand_list.count(item) > max_cnt:
            max_cnt = rand_list.count(item)
            num_max_cnt = item
    print(f'Число встречающееся максимально в списке - {num_max_cnt}, встречается {max_cnt} раз.')


@profile(precision=7)
def hw_3_7():
    from random import randint
    rand_list = [randint(-1000, 1000) for _ in range(200)]
    print(rand_list)
    first_min = min(rand_list)
    rand_list.remove(first_min)
    second_min = min(rand_list)
    print(f'Минимальные числа в массиве {first_min} и {second_min}')


prime_num_for(1000)
prime_eratos(1000)
hw_3_4()
hw_3_7()


'''
Из найденных вариантов, больше всего понравился модуль memory_profiller, с декоратором @profile.
Выдаёт верхнеуровневую оценку потребления памяти выполняемыми функциями,
которая совпадает с наблюдениями по монитору в диспетчере задач Windows.
К сожалению не даёт детального понимания сколько памяти выделено под переменные.
Система windows x64, python 3.10.

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4  20.0898438 MiB  20.0898438 MiB           1   @profile(precision=7)
     5                                         def prime_num_for(i):
     6  20.0976562 MiB   0.0078125 MiB           1       if i < 3:
     7                                                 return i+1
     8  20.0976562 MiB   0.0000000 MiB           1       k = 2
     9  20.0976562 MiB   0.0000000 MiB           1       num = 3
    10  20.1289062 MiB -160.6015625 MiB        7917       while k < i:
    11  20.1289062 MiB -160.5468750 MiB        7916           num += 1
    12  20.1289062 MiB -160.5468750 MiB        7916           prime = True
    13  20.1289062 MiB -119721.2265625 MiB     3712624           for div in range(2, num):
    14  20.1289062 MiB -119703.0390625 MiB     3711626               if num % div == 0:
    15  20.1289062 MiB -142.3828125 MiB        6918                   prime = False
    16  20.1289062 MiB -142.3828125 MiB        6918                   break
    17  20.1289062 MiB -160.6054688 MiB        7916           if prime:
    18  20.1289062 MiB -18.2226562 MiB         998               k += 1
    19  20.0703125 MiB  -0.0585938 MiB           1       del k
    20  20.0703125 MiB   0.0000000 MiB           1       del i
    21  20.0742188 MiB   0.0039062 MiB           1       print(num)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24  20.0937500 MiB  20.0937500 MiB           1   @profile(precision=7)
    25                                         def prime_eratos(i):
    26  20.0937500 MiB   0.0000000 MiB           1       length = i*15
    27  20.8671875 MiB   0.7734375 MiB       15003       num_list = [num for num in range(length)]
    28  20.8671875 MiB   0.0000000 MiB           1       num_list[1] = 0
    29  20.8789062 MiB -100.6406250 MiB       15001       for prime in num_list:
    30  20.8671875 MiB -201.3046875 MiB       15000           if prime:
    31  20.8671875 MiB -10.7812500 MiB       27920               for num in range(prime**2, length, prime):
    32  20.8671875 MiB   0.0000000 MiB       26166                   num_list[num] = 0
    33  20.8593750 MiB  -0.0195312 MiB           1       num_list = sorted(list(set(num_list)))
    34  20.8593750 MiB   0.0000000 MiB           1       del length
    35  20.8593750 MiB   0.0000000 MiB           1       print(num_list[i])


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    38  20.5273438 MiB  20.5273438 MiB           1   @profile(precision=7)
    39                                         def hw_3_4():
    40  20.5273438 MiB   0.0000000 MiB           1       from random import randint
    41  20.5273438 MiB   0.0000000 MiB         103       rand_list = [randint(50, 100) for _ in range(100)]
    42  20.5273438 MiB   0.0000000 MiB           1       rand_set = list(set(rand_list))
    43  20.5273438 MiB   0.0000000 MiB           1       max_cnt = 0
    44  20.5273438 MiB   0.0000000 MiB           1       num_max_cnt = 0
    45  20.5273438 MiB   0.0000000 MiB          41       for item in rand_set:
    46  20.5273438 MiB   0.0000000 MiB          40           if rand_list.count(item) > max_cnt:
    47  20.5273438 MiB   0.0000000 MiB           3               max_cnt = rand_list.count(item)
    48  20.5273438 MiB   0.0000000 MiB           3               num_max_cnt = item
    49  20.5351562 MiB   0.0078125 MiB           1       print(f'Число встречающееся максимально в списке - {num_max_cnt}, встречается {max_cnt} раз.')


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    52  20.5390625 MiB  20.5390625 MiB           1   @profile(precision=7)
    53                                         def hw_3_7():
    54  20.5390625 MiB   0.0000000 MiB           1       from random import randint
    55  20.5390625 MiB   0.0000000 MiB         203       rand_list = [randint(-1000, 1000) for _ in range(200)]
    56  20.5390625 MiB   0.0000000 MiB           1       print(rand_list)
    57  20.5390625 MiB   0.0000000 MiB           1       first_min = min(rand_list)
    58  20.5390625 MiB   0.0000000 MiB           1       rand_list.remove(first_min)
    59  20.5390625 MiB   0.0000000 MiB           1       second_min = min(rand_list)
    60  20.5390625 MiB   0.0000000 MiB           1       print(f'Минимальные числа в массиве {first_min} и {second_min}')
'''