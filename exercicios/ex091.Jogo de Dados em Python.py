# Crie um programa onde 4 jogadores joguem um dados e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dados.
from operator import itemgetter
from random import randint
from time import sleep
jogo = dict()
for c in range(4):
    jogo[f'JOGADOR {c+1}'] = randint(1, 6)
resultado = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=' * 40)
print(f'{"JOGANDO...":^40}')
for k, v in jogo.items():
    sleep(2)
    print(f'{f"O {k}: tirou => {v}":^40}')
print('-' * 40)
print(f'{"RANKING DOS JOGADORES":^40}')
for i, v in enumerate(resultado):
    sleep(1.5)
    print(f'{f"{i + 1}º lugar: {v[0]} => tirou {v[1]}":^40}')
print('=' * 40)
sleep(0.5)
print(f'{"<<< Fim do jogo >>>":^40}')

