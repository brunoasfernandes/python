# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
# Para Binário
# para Octal
# para Hexadecimal
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para EXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Escolha uma opção válida!')

