# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

print('{:=^40}'.format('Lojas do Baratão'))
soma = totmil = menor_preç = cont = nome = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    soma += preço
    print('=' * 20)
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor_preç:
        menor_preç = preço
        nome = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:~^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${soma:.2f}')
print(f'{totmil} produtos acima de R$1000.00')
print(f'O Produto mais barato é {nome} de R${menor_preç:.2f}')
