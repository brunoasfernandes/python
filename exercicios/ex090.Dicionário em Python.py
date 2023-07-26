# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
from typing import Callable

aluno = dict()
semestre = list()
while True:
    aluno['NOME'] = str(input('Nome: ')).upper()
    aluno['MÉDIA'] = float(input(f'Média de {aluno["NOME"]}: '))
    if aluno['MÉDIA'] >= 7:
        aluno['SITUAÇÃO'] = 'Aprovado'
    elif aluno['MÉDIA'] <= 5:
        aluno['SITUAÇÃO'] = 'Reprovado'
    else:
        aluno['SITUAÇÃO'] = 'Recuperação'
    semestre.append(aluno.copy())
    while True:
        resp = str(input('Quer continuar? S/N ')).upper()
        print('-' * 25)
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('-=-' * 15)
for k in aluno.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 45)
for i, v in enumerate(semestre):
    for d in v.values():
        print(f'{d:<15}', end='')
    print()
print('-=-' * 15)




