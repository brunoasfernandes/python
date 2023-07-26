# Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {date.today().year}.')
if idade < 18:
    saldo = 18 - idade
    ano_alist = date.today().year + saldo
    print(f'Ainda falta {saldo} anos para o alistamento!')
    print(f'Seu alistamento será em {ano_alist}.')
elif idade == 18:
    print('É hora de se alistar no serviço militar!')
else:
    saldo = idade - 18
    print(f'Você perdeu o prazo de alistamento, deveria ter se alistado há {saldo} anos.')

