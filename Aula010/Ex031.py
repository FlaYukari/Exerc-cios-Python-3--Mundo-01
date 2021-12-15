print('='*20, 'DESAFIO 031', '='*20)

dist=int(input('Qual é a distância da sua viagem? '))

if dist<=200:
    print(f'Você está prestes a comecar uma viagem de {dist:.2f} Km.\n'
          f'E o preço da passagem será de R$ {dist*0.5:.2f}.')
else:
    print(f'Você está prestes a comecar uma viagem de {dist:.2f} Km.\n'
          f'E o preço da passagem será de R$ {dist * 0.45:.2f}.')

