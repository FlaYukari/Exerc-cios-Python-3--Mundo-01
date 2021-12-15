print('='*20, 'DESAFIO 016', '='*20) #ok

d=int(input('Quantos dias alugados? '))

km=float(input('Quantos km rodados? '))

at= (60 * d) + (0.15*km)

print(f'O total a pagar é de R$ {at:.2f}.')