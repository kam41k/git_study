def medium(arr):
    for i in range(len(arr)):
        m = len(arr)//2
        l = 0
        r = 0
        for j in range(len(arr)):
            if i == j:
                continue
            elif arr[i] < arr[j]:
                r += 1
                if r > m:
                    break
            elif arr[i] > arr[j]:
                l += 1
                if l > m:
                    break
        if l == r == m:
            return arr[i]


from random import randint
m = 9
rand_list = [randint(1, 100) for _ in range(2*m+1)]
print(rand_list)
print(medium(rand_list))
