# Adapte o código do desafio #107, criando uma função adicional chamada moedas()
# que consiga mostrar os números como um valor monetário formatado.
from ex111 import moedas
v = float(input('Digite um valor: '))
print(f'O valor {moedas.moeda(v)} mais 30% é: {moedas.moeda(moedas.aumentar(v, 30))}')
print(f'O valor {moedas.moeda(v)} menos 45% é: {moedas.moeda(moedas.reduzir(v, 45))}')
print(f'O valor {moedas.moeda(v)} dobrado é: {moedas.moeda(moedas.dobro(v))}')
print(f'O valor {moedas.moeda(v)} pela metade é: {moedas.moeda(moedas.metade(v))}')

