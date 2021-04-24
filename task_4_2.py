def currency_rates(currency):
    """
    Get foreign currency rate to Russian Ruble, from Russian Central Bank site.

    :param currency: foreign currency code("USD" , "EUR" etc.)
    :return: foreign currency rate to rub. Class - Decimal(Float). 'None' if wrong currency code
    """
    from requests import get
    from decimal import Decimal

    currency_market = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency = currency.upper()
    if currency in currency_market:
        '''
        Расчет с типом данных Float.
        '''
        # currency_value = round(float(currency_market.partition(currency)[2].partition('NumCode')[0].
        #                              partition('<Value>')[2].partition('</Value>')[0].replace(',', '.')), 2)
        # currency_nominal = int(currency_market.partition(currency)[2].partition('NumCode')[0].
        #                        partition('<Nominal>')[2].partition('</Nominal>')[0])
        # currency_rate = round(currency_value/currency_nominal, 2)
        '''
        Расчет с типом данных Decimal.
        '''
        currency_value = Decimal(currency_market.partition(currency)[2].partition('NumCode')[0].partition('<Value>')[2]
                                 .partition('</Value>')[0].replace(',', '.')).quantize(Decimal('.00'))
        currency_nominal = int(currency_market.partition(currency)[2].partition('NumCode')[0].
                               partition('<Nominal>')[2].partition('</Nominal>')[0])
        currency_rate = currency_value/currency_nominal
        return currency_rate
    else:
        return None


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates("eur"))
    print(currency_rates('GBR'))
