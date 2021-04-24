from utils import currency_rates
from sys import argv

if len(argv) > 1:
    currency = argv[1]
else:
    currency = 'USD'

print(currency_rates(currency))
