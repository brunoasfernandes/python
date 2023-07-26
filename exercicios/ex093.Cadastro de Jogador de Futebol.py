# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.
scout = dict()
gols = list()
scout['NOME'] = str(input('Nome do jogador: ')).upper().strip()
partidas = int(input(f'Quantas partidas o {scout["NOME"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols {scout["NOME"]} fez na {c +1}ª partida? ')))
    scout['GOLS'] = gols[:]
    scout['TOTAL GOLS'] = sum(gols)
print('-' * 40)
print(f'{"=== SCOUT DO JOGADOR ===":^40}')
for i, v in enumerate(scout['GOLS']):
    print(f'       -Na {i + 1}ª partida {scout["NOME"]} fez {v}')
print(f'       -Total de gols: {scout["TOTAL GOLS"]}')
print('-' * 40)







