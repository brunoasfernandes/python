# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))

# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

# verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior valor digitado foi: {}'.format(maior))
print(f'O menor valor digitado foi: {menor}')

