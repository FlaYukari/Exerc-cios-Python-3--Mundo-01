print('='*20, 'DESAFIO 022', '='*20)

n=int(input('Informe um número: '))

u= n%10
d=n//10
dd=str(d)
c=n//100
cc=str(c)
m=n//1000
print(f'Analisando o número {n}:')
print(f'Unidade: {u}')
print(f'Dezena: {dd[-1]}')
print(f'Centena: {cc[-1]}')
print(f'Milhar: {m}')