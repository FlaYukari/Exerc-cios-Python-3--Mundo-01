print('='*20, 'DESAFIO 06', '=' *20) #OK

n = int(input('Escolha um número que calcularemos o dobro, o triplo e sua raiz quadrada: \n'))

d = n * 2

t = n * 3

rq = n**(1/2) #rq = pow(n, (1/2)

print(f'a) O dobro de {n} é: {d};\nb) O triplo de {n} é: {t}; e\nc) A raiz quadrada de {n} é: {rq:.2f}.')