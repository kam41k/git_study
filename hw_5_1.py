from collections import defaultdict

org_profit = defaultdict(list)
n = int(input('Введите количество организаций: '))
all_profit = 0
for org in range(n):
    org_name = input('Введите название организации: ')
    for quart in range(1, 5):
        profit = input(f'Введите прибыль за {quart} квартал, для организации - {org_name}: ')
        org_profit[org_name].append(int(profit))
    org_pr = sum(org_profit[org_name])      # Общая прибыль за год для организации.
    all_profit += org_pr                    # Общая прибыль по всем организациям.
    org_profit[org_name].append(org_pr)
mid_profit = all_profit / n                 # Определяем среднюю прибыль.
print('Предприятия с прибылью выше среднего:')
for org, profit in org_profit.items():
    if profit[-1] > mid_profit:
        print(f'{org} - {profit[-1]}')
print('Предприятия с прибылью ниже среднего:')
for org, profit in org_profit.items():
    if profit[-1] < mid_profit:
        print(f'{org} - {profit[-1]}')
