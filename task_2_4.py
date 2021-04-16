empl_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee in empl_list:
    print(f'Привет, {employee.split(" ")[-1].capitalize()}!')
