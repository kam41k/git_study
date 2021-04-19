def num_translate_adv(en_num):
    num_dict = {'zero': 'ноль', 'one': 'один',
                'two': 'два', 'three': 'три',
                'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь',
                'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
                }
    if en_num.istitle() and en_num.lower() in num_dict:
        print(num_dict.get(en_num.lower()).capitalize())
    else:
        print(num_dict.get(en_num))


num_translate_adv('One')
num_translate_adv("two")
num_translate_adv("twelve")
num_translate_adv('Eleven')
