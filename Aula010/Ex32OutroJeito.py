print('='*20, 'DESAFIO 032 - Outro Jeito', '='*20)

import datetime
ano=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano=datetime.date.today().year

if ano%4==0 or ano%400==0:
    print(f'O ano {ano} é BISSEXTO.')

else:
    print(f'O ano {ano} NÃO é BISSEXTO.')