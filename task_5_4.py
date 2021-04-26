src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for _, num in zip(src, src[1:]) if num > _]
print(result)
