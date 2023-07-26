# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no finaldo jogo.
from random import randint
vit = 0
print('-=' * 15)
print(f'{"Vamos jogar PAR ou ÍMPAR":^30}')
print('-=' * 15)
while True:
    jogada = int(input('Par ou Ímpar [0/1]: '))
    joga = int(input('Digite um valor entre 0 e 5: '))
    comp = randint(0, 5)
    print(f'Computador: {comp}\nJogador: {joga}')
    if jogada == 0:
        if (joga + comp) % 2 == 0:
            print(f'Jogador venceu! {joga + comp} é PAR!')
        else:
            print(f'Computador venceu! {joga + comp} é ÍMPAR')
            break
    elif jogada == 1:
        if (joga + comp) % 2 == 1:
            print(f'Jogador venceu! {joga + comp} é ÍMPAR')
        else:
            print(f'Computador venceu! {joga + comp} é PAR')
            break
    print('-=' * 15)
    vit += 1

print(f'{vit} vitórias consecutivas para o jogador.')
print(f'{"<<<< GAME OVER >>>>>":^30}')
print('-=-' * 15)









