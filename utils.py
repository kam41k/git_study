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


def currency_rates_et(inp_cur_code):
    from requests import get
    from datetime import date
    from decimal import Decimal
    import xml.etree.ElementTree as ET

    currency_market = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    inp_cur_code = inp_cur_code.upper()
    if inp_cur_code in currency_market:
        currency_market_et = ET.fromstring(currency_market)
        currency_rate_date = currency_market_et.attrib['Date'].split('.')
        currency_rate_date = date(day=int(currency_rate_date[0]), month=int(currency_rate_date[1]),
                                  year=int(currency_rate_date[2]))
        for valute in currency_market_et.iter('Valute'):
            if valute.find('CharCode').text == inp_cur_code:
                currency = valute.find('CharCode').text
                currency_value = Decimal(valute.find('Value').text.replace(',', '.')).quantize(Decimal('.00'))
                currency_nominal = valute.find('Nominal').text
                return f'{currency_value} RUB for {currency_nominal} {currency}, {currency_rate_date}'
    else:
        return None


def currency_rates_soup(inp_cur_code):
    from requests import get
    from datetime import date
    from bs4 import BeautifulSoup
    currency_market = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    inp_cur_code = inp_cur_code.upper()
    if inp_cur_code in currency_market:
        currency_market = BeautifulSoup(currency_market, 'lxml')
        currencies = currency_market.find_all('valute')
        currency_rate_date = currency_market.find('valcurs').attrs['date'].split('.')
        currency_rate_date = date(day=int(currency_rate_date[0]), month=int(currency_rate_date[1]),
                                  year=int(currency_rate_date[2]))
        for currency in currencies:
            currency_code = currency.find('charcode').text
            if currency_code == inp_cur_code:
                currency_value = round(float(currency.find('value').text.replace(',', '.')), 2)
                currency_nominal = currency.find('nominal').text
                return f'{currency_value} RUB for {currency_nominal} {currency_code}, {currency_rate_date}'
    else:
        return None
