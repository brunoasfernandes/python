# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1, 5+1):
    peso = float(input(f'Qual o peso da {p}ª Pessoa? '))
    if p == 1:     # verificando a primeira ocorrência
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O MAIOR peso lido é {maior}kg')
print(f'O MENOR peso lido é {menor}kg')