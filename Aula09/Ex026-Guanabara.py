print('='*20, 'DESAFIO 026', '='*20)

frase=str(input('Digite uma frase: ').strip().upper())
print(f'A letra A apareceu {frase.count("A")} vezes na frase. '
      f'\nA primeira letra A apareceu na posição {frase.find("A")+1}. '
      f'\nA última letra A apareceu na posição {frase.rfind("A")+1}.')
