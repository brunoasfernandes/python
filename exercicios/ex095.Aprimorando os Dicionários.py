# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
gols_partida = list()
lista_final = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).upper().strip()
    tot = int(input(f'    Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        gols_partida.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
    jogador['gols'] = gols_partida[:]
    jogador['total'] = sum(gols_partida)
    lista_final.append(jogador.copy())
    gols_partida.clear()
    while True:
        resp = str(input('Quer continuar? S/N ')).upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('-=' * 20)
print('cod ', end='')
for k in jogador.keys():  # cabaçalho com as chaves do dicionário
    print(f'{k:<15}', end='')
print()
print('-=' * 20)
for i, v in enumerate(lista_final):
    print(f'{i:>2}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('~' * 40)
while True:
    busca = int(input('Scout de qual jogador quer mostrar? (999 p/ sair) '))
    print('~' * 40)
    if busca == 999:
        break
    if busca >= len(lista_final):
        print(f'ERRO! jogador {busca} não encontrado.')
    else:
        print(f'Scout do jogador {lista_final[busca]["nome"]}:')
        for i, g in enumerate(lista_final[busca]['gols']):
            print(f'   No  {i + 1}º jogo fez {g} gols.')



