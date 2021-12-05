num_list = [8, 3, 15, 6, 4, 2]
idx_list = [idx for idx, num in enumerate(num_list) if num % 2 == 0]
# for idx, num in enumerate(num_list):
#     if num % 2 == 0:
#         idx_list.append(idx)
print(idx_list)
print(max(num_list))

