def prc_decl(perc):
    if perc == 0:
        print(f'{perc} процентов')
    elif perc == 1:
        print(f'{perc} процент')
    elif perc <= 4:
        print(f'{perc} процента')
    else:
        print(f'{perc} процентов')

prc_decl(0)
prc_decl(1)
prc_decl(3)
prc_decl(14)
