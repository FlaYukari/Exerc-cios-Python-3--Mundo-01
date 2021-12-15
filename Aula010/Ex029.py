print('='*20, 'DESAFIO 029', '='*20)

velocidade=int(input('Qual é a velocidade do carro? '))

#Condição SIMPLES:
if velocidade>80:
    multa = ((velocidade - 80)*7)
    print('\n\33[31mMULTADO! Você excedeu o limite permitido que é de 80 km/h.'
          'Você deve pagar uma multa de R$ {:.2f}\33[m\n'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')