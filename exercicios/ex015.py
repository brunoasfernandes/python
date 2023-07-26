# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado a quantidade de dias quais ele foi alugado.
# Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

dias = int(input('Quantos dias alugado? '))
km_rodados = float(input('Quantos km rodados? '))
total_pagar = (dias * 60) + (km_rodados * 0.15)
print('O total a pagar é R${:.2f}'.format(total_pagar))




