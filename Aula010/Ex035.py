print('='*20, 'DESAFIO 035', '='*20)

p=float(input('Primeiro seguimento: '))
s=float(input('Segundo seguimento: '))
t=float(input('Terceiro seguimento: '))

if p<(s+t) and s<(p+t) and t<(p+s):
    print('Os seguimentos acima PODEM FORMAR triângulo.')
    if p!=s!=t!=p: #CUIDADO!!! p também tem q ser diferente de t
        print('Esse triângulo é ESCALENO.')
    elif p==s==t:
        print('Esse triângulo é EQUILÁTERO.')
    else:
        print('Esse triângulo é ISÓSSELES.')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo.')
