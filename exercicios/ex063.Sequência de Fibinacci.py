# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
# N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('=' * 22)
print('Sequência de Fibonacci')
print('=' * 22)

termo = int(input('Quantos termos você quer mostrar?: '))
termo1 = 0
termo2 = 1
cont = 3

print(f'{termo1}, {termo2}', end=', ')
while cont <= termo:
    termos = termo1 + termo2
    termo1 = termo2
    termo2 = termos
    cont += 1
    print(f'{termos}', end=', ')
print('FIM')
