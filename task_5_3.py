def tutor_klass_tools(tutors_list, klasses_list):
    if len(tutors_list) > len(klasses_list):
        from itertools import zip_longest
        for tutor, klass in zip_longest(tutors_list, klasses_list):
            yield tutor, klass
    else:
        for tutor, klass in zip(tutors_list, klasses_list):
            yield tutor, klass


def tutor_klass(tutors_list, klasses_list):
    if len(tutors_list) > len(klasses_list):
        for _ in range(len(tutors_list)-len(klasses_list)):
            klasses_list.append(None)
    for tutor, klass in zip(tutors_list, klasses_list):
        yield tutor, klass


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Владимир']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
tutors_klasses = tutor_klass(tutors, klasses)
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
