# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

computador = randint(0, 10)
palpite = 0
acertou = False

print('-=-' * 20)
print('Olá, sou seu Computador...\nVou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
sleep(4)
while not acertou:
    print('~' * 28)
    jogador = int(input('Em que número eu pensei? '))
    palpite += 1
    if jogador == computador:
        acertou = True
        sleep(1.5)
        print('~' * 28)
        print('Parabéns! você conseguiu me vencer!')
        print(f'Eu pensei no número {computador}')
        print(f'Foram necessários {palpite} palpites. ')
    else:
        if jogador < computador:
            sleep(1.5)
            print('Mais... Tente novamente!')
        elif jogador > computador:
            sleep(1.5)
            print('Menos... Tente novamente!')
print('FIM do Jogo!')
