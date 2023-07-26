# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=-' * 4)
print('Gerador de PA')
print('-=-' * 4)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
print('PA:', end=' ')
while cont <= 10:
    print(f'{termo}', end=', ')
    termo += razao
    cont += 1
print('FIM')

