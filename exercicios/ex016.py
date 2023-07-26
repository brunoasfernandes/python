# Crie um programa que leia um número Real qualquer pelo teclado e mostre na leta a sua porção inteira.
'''num = float(input('Digite um número Real: '))
print('A porção inteira de {} é: {}.'.format(num, int(num)))'''

from math import trunc
num = float(input('Digite um número Real: '))
print('A porção inteira do {} é: {}.'.format(num, trunc(num)))



