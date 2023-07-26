# Crie um módulo chamado moedas.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from ex111 import moedas
v = float(input('Digite um valor: '))
print(f'O valor {v} mais 30% é: {moedas.aumentar(v, 30)}  ')
print(f'O valor {v} menos 45% é: {moedas.reduzir(v, 45)} ')
print(f'O valor {v} dobrado é: {moedas.dobro(v)}')
print(f'O valor {v} pela metade é: {moedas.metade(v)} ')
