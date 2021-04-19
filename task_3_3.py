def thesaurus(*args):
    employee_dict = {}
    for employee in args:
        employee_dict.setdefault(employee[0], [])
        employee_dict[employee[0]].append(employee)
    return employee_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))

'''
Сортировка словаря с сотрудниками по ключу
'''
employee_dict_to_sort = thesaurus('Петр', 'Мария', 'Иван', 'Илья')
print(employee_dict_to_sort)
employee_dict_to_sort = dict(sorted(employee_dict_to_sort.items(), key=lambda _item: _item[0]))
print(employee_dict_to_sort)
