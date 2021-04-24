def currency_rates(currency):
    """
    Get foreign currency rate to Russian Ruble, from Russian Central Bank site.

    :param currency: foreign currency code("USD" , "EUR" etc.)
    :return: Str contains foreign currency rate and date of request. 'None' if wrong currency code
    """
    from requests import get
    from decimal import Decimal
    from datetime import date

    currency_market = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency = currency.upper()
    currency_rate_date = currency_market.partition('Date="')[2].partition('"')[0].split('.')
    currency_rate_date = date(day=int(currency_rate_date[0]), month=int(currency_rate_date[1]),
                              year=int(currency_rate_date[2]))
    if currency in currency_market:
        '''
        Расчет с типом данных Float.
        '''
        # currency_value = round(float(currency_market.partition(currency)[2].partition('NumCode')[0].
        #                              partition('<Value>')[2].partition('</Value>')[0].replace(',', '.')), 2)
        # currency_nominal = int(currency_market.partition(currency)[2].partition('NumCode')[0].
        #                        partition('<Nominal>')[2].partition('</Nominal>')[0])
        '''
        Расчет с типом данных Decimal.
        '''
        currency_value = Decimal(currency_market.partition(currency)[2].partition('NumCode')[0].partition('<Value>')[2]
                                 .partition('</Value>')[0].replace(',', '.')).quantize(Decimal('.00'))
        currency_nominal = int(currency_market.partition(currency)[2].partition('NumCode')[0].
                               partition('<Nominal>')[2].partition('</Nominal>')[0])
        return f'{currency_value} RUB for {currency_nominal} {currency}, {currency_rate_date}'
    else:
        return None


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('sek'))
    print(currency_rates('EURO'))
