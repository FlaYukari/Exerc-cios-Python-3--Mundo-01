print('='*20, 'DESAFIO 034', '='*20)

salario=int(input('Qual o valor do funcionário? '))

if salario>1250:
    aumento = salario*(1.1)
else:
    aumento=salario*(1.15)

print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {aumento:.2f} agora.')