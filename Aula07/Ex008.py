print('='*20,'DESAFIO 008', '='*20) #OK

print('Você sabe transformar medidas em metros para centímetros, milímetros e polegadas? Vou calcular para você!\n')

n = float(input('Escreva a medida EM METROS que você queira converter para centímetros, milímetros e polegadas: '))

p = (n*100 / 2.54)

print(f'Muito bem, {n} metros é o mesmo que {(n*100):.2f} centímetros, o mesmo que {(n*1000):.2f} milímetros e o mesmo que {p:.2f} polegadas.')