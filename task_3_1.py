def num_translate(en_num):
    num_dict = {'zero': 'ноль', 'one': 'один',
                'two': 'два', 'three': 'три',
                'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь',
                'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
                }
    print(num_dict.get(en_num))


num_translate('one')
num_translate('eight')
num_translate('eleven')
