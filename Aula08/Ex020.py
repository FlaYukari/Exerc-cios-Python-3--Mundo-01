print('='*20, 'DESAFIO 020', '='*20) #ok

from random import sample, shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista=[a1, a2, a3, a4]

print(f'A ordem de apresentação será {sample(lista, 4)}.')


shuffle(lista)
print(f'A ordem de apresentação será {lista}.')