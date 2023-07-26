# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e enquantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou o empréstimo não será aprovado.

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
prazo = int(input('Em quantos anos vai pagar? '))
prazo = prazo * 12
parcela = casa / prazo
minimo = salario * 30 / 100

if parcela <= minimo:
    print('Parabéns o seu empréstimo foi aprovado')
    print(f'{prazo} vezes de R${parcela:.3f}')
else:
    print('Empréstimo não aprovado.')
    print('O valor da parcela não pode ser maior que 30% do salario do cliente!')

