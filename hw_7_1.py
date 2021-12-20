from random import randint
rand_list = [randint(-100, 100) for _ in range(20)]
print(rand_list)
'''
Улучшение алгоритма сортировки - ввод переменной(счетчика), 
которая следит за тем, была ли за проход хотя бы одна перестановка.
Если перестановок небыло, массив считается отсортированным и цикл завершается.
'''
k = 1
n = 1
while k == 1:
    k = 0
    for i in range(len(rand_list)-n):
        if rand_list[i] < rand_list[i+1]:
            rand_list[i], rand_list[i+1] = rand_list[i+1], rand_list[i]
            k = 1
    n += 1
print(rand_list)
