# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

cont_maior = 0
cont_menor = 0

for c in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento {c}ª Pessoa? '))
    idade = date.today().year - ano_nasc
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'{cont_maior} pessoas já atingiram a maior idade.')
print(f'{cont_menor} pessoas ainda não atingiram a maior idade.')
