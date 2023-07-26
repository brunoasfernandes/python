# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
# DIFICUDADE
media_idade = 0
soma_idade = 0
idade_homem_mais_v = 0
nome_homem_mais_v = ''
total_mulher = 0

for p in range(1, 5):
    print(f'----- {p}ª Pessoa -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade

    if p == 1 and sexo == 'M':
        idade_homem_mais_v = idade
        nome_homem_mais_v = nome
    if sexo == 'M' and idade > idade_homem_mais_v:
        idade_homem_mais_v = idade
        nome_homem_mais_v = nome
    if sexo == 'F' and idade < 20:
        total_mulher += 1
media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {idade_homem_mais_v} anos e se chama {nome_homem_mais_v}.')
print(f'Ao todo são {total_mulher} mulheres com menos de 20 anos')
