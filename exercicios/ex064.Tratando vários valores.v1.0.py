# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = soma = numeros = 0

numeros = int(input('Digite um número ou (999) para sair: '))
while numeros != 999:
    cont += 1
    soma += numeros
    numeros = int(input('Digite um número ou (999) para sair: '))

print('~' * 40)
print(f'Foram digitados {cont} números.')
print(f'A soma dos números digitados é: {soma}')
