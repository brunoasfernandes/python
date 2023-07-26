# Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
maquina = randint(0 ,2)

print('''Que comecem os jogos!
Suas opções:
PEDRA   [0]
PAPEL   [1]
TESOURA [2]''')
jogador = int(input('Faça sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print(f'Máquina jogou {itens[maquina]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if jogador == 0: # jogador jogou pedra
    if maquina == 0:
        print('Empate!')
    elif maquina == 1:
        print('Máquina venceu!')
    elif maquina == 2:
        print('Jogador venceu!')

elif jogador == 1: # jogador jogou papel
    if maquina == 0:
        print('Jogador venceu!')
    elif maquina == 1:
        print('Empate!')
    elif maquina == 2:
        print('Maquina venceu!')

elif jogador == 2: # jogador jogou tesoura
    if maquina == 0:
        print('Máquina venceu!')
    elif maquina == 1:
        print ('Jogador venceu!')
    elif maquina == 2:
        print('Empate!')
else:
    print('Jogada inválida')

