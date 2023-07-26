# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
parar = 'S'
numeros = cont = soma = media = maior = menor = 0
while parar in 'S':
    print('~' * 30)
    numeros = int(input('Digite um valor: '))
    soma += numeros
    cont += 1
    if cont == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    parar = str(input('Deseja digitar outro valor? [S] para SIM / [N] para NÃO ')).upper().strip()[0]
media = soma / cont
print('-' * 30)
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior número lido foi: {maior}')
print(f'O menor número lido foi: {menor}')

