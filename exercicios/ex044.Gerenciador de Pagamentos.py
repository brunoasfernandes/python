# Elabore um programa que calcule o valor a ser pago por um produto, considerando o preso mormal e condição de pagamento:
# À vista dinheiro ou cheque: 10% de desconto.
# À vista cartão: 5% de desconto.
# Em até 2x no cartão: Preso normal.
# Em 3x ou mais no cartão: 20% de juros.

valor = float(input('Valor das compras R$: '))
pagamento = int(input('''Escolha uma das opções abaixo!
[1] À vista dinheiro/cheque:
[2] À vista no cartão:
[3] Em até 2x no cartão:
[4] 3x ou mais no cartão:
Qual a opção de pagamento? '''))

if pagamento == 1:
    preço_final = valor - (valor * 10 / 100)
    print(f'Total com 10% de desconto: R${preço_final:.2f}')
elif pagamento == 2:
    preço_final = valor - (valor * 5 / 100)
    print(f'Total com 5% de desconto: R${preço_final:.2f}')
elif pagamento == 3:
    preço_final = valor
    parcela = valor / 2
    print(f'Em 2x de R${parcela:.2f}')
    print(f'Total sem juros: R${preço_final:.2f}')
elif pagamento == 4:
    preço_final = valor + (valor * 20 / 100)
    totparc = int(input('Em quantas vezes ? '))
    parcela = valor / totparc
    print(f'Em {totparc}x de R${parcela:.2f}. ')
    print(f'Total com 20% de juros: R${preço_final:.2f}')
else:
    total = 0
    print('\033[7;31mOPÇÃO DE PAGAMENTO INVÁLIDA! Tente novamente.\033[m')
