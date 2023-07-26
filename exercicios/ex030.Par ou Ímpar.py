# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número '))
resultado = numero % 2
if resultado == 0:
    print('\033[1;7mEsse número é Par!\033[m')
else:
    print('\033[1;7mEsse número é Ímpar!\033[m')




