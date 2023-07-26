# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moedas(), desenvolvida no desafio 108.
from ex111 import moedas
v = float(input('Digite um valor: '))
print(f'O valor {moedas.moeda(v)} mais 30% é: {moedas.aumentar(v, 30, True)}')
print(f'O valor {moedas.moeda(v)} menos 45% é: {moedas.reduzir(v, 45, True)}')
print(f'O valor {moedas.moeda(v)} dobrado é: {moedas.dobro(v, True)}')
print(f'Metade  do valor {moedas.moeda(v)} é: {moedas.metade(v, False)}')
