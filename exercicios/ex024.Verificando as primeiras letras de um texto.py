# Crie um programa que leia o nome de uma cidade
# e dia se ela começa ou não com "SANTO".

cidade = str(input('Em qual cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')



