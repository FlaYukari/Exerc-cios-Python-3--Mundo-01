print('='*20, 'DESAFIO 017', '='*20) #ok

co=float(input('Digite o valor em centímetros do cateto oposto de um triângulo retângulo: '))

ca=float(input('Digite o valor em centímetros do cateto adjacente de um triângulo retângulo: '))

hip= pow((co ** 2 + ca ** 2), 1/2)

print(f'O valor da hipotenusa de um triângulo retângulo que possui cateto oposto e adjacente medindo {co:.2f} e {ca:.2f}, respectivamente, é de {hip:.2f} centímetros.')

import math # ou from math import hypot

hi=math.hypot(co, ca) # hi=hypot(co, ca)

print(f'Hipotenusa vale: {hi}')