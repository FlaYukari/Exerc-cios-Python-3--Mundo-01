#from random import randint
import random
import time

print('='*20, 'DESAFIO 028', '='*20)

print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')

computador = random.randint(0, 5)

resposta=int(input('Em que número pensei? '))
print('PROCESSANDO.....')
time.sleep(3)

if resposta == computador:
    print('Parabéns!! Você acertou!!')
else:
    print('Que pena, você errou, pensei no número {}'.format(computador))

print('--FIM--')

