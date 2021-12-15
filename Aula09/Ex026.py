print('='*20, 'DESAFIO 026', '='*20)
import unicodedata as ud

frase=str(input('Digite uma frase: ').strip().upper())
tireiacento=ud.normalize('NFD', frase)
print(f'A letra A apareceu {tireiacento.count("A")} vezes na frase. '
      f'\nA primeira letra A apareceu na posição {tireiacento.find("A")+1}. '
      f'\nA última letra A apareceu na posição {tireiacento.rfind("A")+1}.')
