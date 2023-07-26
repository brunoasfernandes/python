# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: ')).upper()
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['ctps'] = int(input('Nº carteira de trabalho (0 não tem) '))
if trabalhador['ctps'] == 0:
    trabalhador['ctps'] = 'NÃO TEM'
elif trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = (35 + trabalhador['contratação'] + trabalhador['idade']) - datetime.now().year
print('~' * 30)
print(f'{"TRABALHADOR":^30}')
for k, v in trabalhador.items():
    print(f'{k:<15} {v:>14}')
print('~' * 30)
