print('='*20, 'DESAFIO 018', '='*20) #ok

from math import radians, degrees, sin, cos, tan

a=float(input('Digite o ângulo que você deseja: '))

print(f'O ângulo de {a} tem o SENO de {sin(radians(a)):.2f}.\nO ângulo de {a} tem o COSSENO de {cos(radians(a)):.2f}.\nO ângulo de {a} tem o COSSENO de {tan(radians(a)):.2f}.')