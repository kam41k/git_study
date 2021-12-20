def sort_merge(arr):
    if len(arr) <= 1:
        return arr
    half_1 = sort_merge(arr[0:len(arr)//2])
    half_2 = sort_merge(arr[len(arr)//2:])
    result = []
    k = 0
    n = 0
    while (k < len(half_1) and n < len(half_2)):
        if half_1[k] <= half_2[n]:
            result.append(half_1[k])
            k += 1
        elif half_1[k] > half_2[n]:
            result.append(half_2[n])
            n += 1
    while k < len(half_1):
        result.append(half_1[k])
        k += 1
    while n < len(half_2):
        result.append(half_2[n])
        n += 1
    return result


from random import uniform
rand_list = [round(uniform(0, 50), 2) for _ in range(16)]
print(rand_list)
print(sort_merge(rand_list))
