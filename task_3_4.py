def thesaurus_adv(*args):
    employee_dict = {}
    for employee in args:
        employee_dict.setdefault(employee.split(' ')[1][0], {})
        employee_dict[employee.split(' ')[1][0]].setdefault(employee.split(' ')[0][0], [])
        employee_dict[employee.split(' ')[1][0]][employee.split(' ')[0][0]].append(employee)
    return employee_dict


employee_dict_to_sort = thesaurus_adv('Иван Сергеев', 'Петр Алексеев', 'Яна Юшкевич',
                                      'Инна Серова', 'Анна Савельева', 'Илья Иванов')
print(employee_dict_to_sort)

'''
Двойная сортировка, по ключам имён внутренних словарей и по ключам фамилий основного.
'''
for key, item in employee_dict_to_sort.items():
    employee_dict_to_sort[key] = dict(sorted(item.items(), key=lambda _item: _item[0]))
employee_dict_to_sort = dict(sorted(employee_dict_to_sort.items(), key=lambda _item: _item[0]))
print(employee_dict_to_sort)
