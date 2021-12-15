print('='*20, 'DESAFIO 025', '='*20)

nome=str(input('Qual é seu nome completo? ').strip().upper())
print('Seu nome tem Silva? ', end='')
if 'SILVA' in nome:
    print('True')
else:
    print('False')