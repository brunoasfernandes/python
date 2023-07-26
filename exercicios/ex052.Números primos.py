# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(c, end=', ')

print(f'\n\033[mO número {num} é dividido {total} vezes.')
if total == 2:
    print('Portanto ELE É PRIMO!')
else:
    print('Portanto ele NÃO É PRIMO!')