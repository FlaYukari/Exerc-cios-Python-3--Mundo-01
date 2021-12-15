print('='*20, 'DESAFIO 027', '='*20)

nomec=str(input('Digite seu nome completo: ').strip())
lnomec=nomec.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {lnomec[0]}.')
print(f'Seu último nome é {lnomec[-1]}.') # ou {lnomec[len(lnomec)-1]}
