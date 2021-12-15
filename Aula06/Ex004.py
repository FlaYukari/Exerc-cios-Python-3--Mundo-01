print('='*20, 'DESAFIO 04', '='*20) #OK

coisa = input('Escreva algo: ')

print('O tipo primitivo desse valor é ',type(coisa))
print('O valor só possui espaços? ', coisa.isspace())
print('O valor é um número? ', coisa.isnumeric())
print('O valor é alfabético? ', coisa.isalpha())
print('O valor é alfanumérico? ', coisa.isalnum())
print('O valor está em maiúsculo? ', coisa.isupper())
print('O valor está em minúsculo? ', coisa.islower())
print('O valor é nome próprio? ', coisa.istitle()) #capitalizada
print('Quantos elementos possui o valor? ', len(coisa))