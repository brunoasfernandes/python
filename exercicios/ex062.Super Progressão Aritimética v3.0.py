print('~' * 14)
print('Gerador de PA')
print('~' * 14)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('-' * 14)
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=', ')
        cont += 1
        termo += razao
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('-' * 45)
print(f'Progressão finalizada com {total} termos mostrados.')
