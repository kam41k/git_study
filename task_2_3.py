str_list = ['в', '5', 'часов', '17',
            'минут', 'температура', 'воздуха',
            'была', '+5', 'градусов']

indx_increase = 0
for indx, elem in enumerate(str_list.copy()):
    if elem.isdigit():
        str_list[indx+indx_increase] = f'{int(elem):02}'
        str_list.insert(indx+indx_increase+1, '"')
        str_list.insert(indx+indx_increase, '"')
        indx_increase += 2
    elif elem[0] in ['+', '-']:
        if elem[1:].isdigit():
            str_list[indx+indx_increase] = f'{int(elem):+03}'
            str_list.insert(indx + indx_increase + 1, '"')
            str_list.insert(indx + indx_increase, '"')
            indx_increase += 2

print(' '.join(str_list))

'''
Склеиваем строку вручную, что бы избавиться от пробелов в кавычках.
'''
result_str = ''
for indx, elem in enumerate(str_list[:]):
    try:
        if (elem.isdigit() or elem[0] in ['+', '-'] and elem[1:].isdigit()) or elem == '"' and (str_list[indx+1].isdigit() or str_list[indx+1][0] in ['+', '-'] and str_list[indx+1][1:].isdigit()):
            result_str = f'{result_str}{elem}'
        else:
            result_str = f'{result_str}{elem} '
    except IndexError:
        result_str = f'{result_str}{elem}'
print(result_str)
