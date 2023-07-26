from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for j in range(0, 4):
    jogadores[f'Jogador {j+1}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('='*30)
print('          ==RANKING==')
contador = 1
for x in range(0, len(ranking)):
    if x == 0:
        print(f'  {contador}º - {ranking[x][0]} com {ranking[x][1]} pontos.')
    elif ranking[x][1] == ranking[x - 1][1]:
        print(f'       {ranking[x][0]} com {ranking[x][1]} pontos.')
    else:
        contador += 1
        print(f'  {contador}º - {ranking[x][0]} com {ranking[x][1]} pontos.')