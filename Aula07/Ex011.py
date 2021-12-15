print('='*20, 'DESAFIO 011', '='*20) #ok

a = float(input('Vamos calcular a quantidade de tinta necessária para pintar uma parede. \n\nPara isso, me informe em metros a altura da sua parede: '))

l = float(input('Agora é necessária a largura da sua parede em metros: '))

print('A quantidade de litros de tinta necessária para pintar uma parede de área {:.2f} m² é de {:.2f} litros.'.format(a*l, (a*l)/2))