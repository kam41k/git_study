import random


def get_jokes(jokes_num, repeats=True):
    """
    Printing a list of jokes

    :param jokes_num: numbers of jokes in list
    :param repeats: repeats of words in jokes(default = True)
    """
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
    jokes = []
    for i in range(jokes_num):
        try:
            noun, adverb, adjective = random.choice(nouns), random.choice(adverbs), random.choice(adjectives)
            jokes.append(f'{noun} {adverb} {adjective}')
            if not repeats:
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
        except IndexError:
            print('Возможные шутки закончились')
    print(jokes)


get_jokes(2)
get_jokes(4)
