# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
para = ' '
c_idade = c_homem = c_mulher = 0

print('-=-' * 7)
print('Cadastro de pessoas')
print('-=-' * 7)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('ERRO: Digite M para masculino ou F para feminino ')).upper().strip()[0]
    print('~' * 23)
    if idade > 18:
        c_idade += 1
    if sexo == 'M':
        c_homem += 1
    if sexo == 'F' and idade < 20:
        c_mulher += 1

    para = str(input('Quer continua? [S/N] ')).upper().strip()[0]
    while para not in 'SN':
        para = str(input('ERRO: Digite S para sim ou N para não ')).upper().strip()[0]
    if para == 'N':
        break


print(f'Foram cadastradas {c_idade} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {c_homem} homens.')
print(f'Foram cadastradas {c_mulher} mulheres menores de 20 anos.')