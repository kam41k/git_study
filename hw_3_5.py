from random import randint
rand_list = [randint(-100, 100) for i in range(20)]
print(rand_list)
neg_list = [i for i in rand_list if i < 0]
print(f'Максимальное отрицательное число - "{max(neg_list)}", индекс - {rand_list.index(max(neg_list))}')
