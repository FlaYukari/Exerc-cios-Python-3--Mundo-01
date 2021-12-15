print('='*20, 'DESAFIO 031 - DIFERENTE', '='*20)

dist=float(input('Qual é a distância da sua viagem? '))

preco=float(dist*0.5 if dist<=200 else dist*0.45)

print(f'Você está prestes a comecar uma viagem de {dist:.2f} Km.'
      f'\nE o preço da passagem será de R$ {preco:.2f}.')


