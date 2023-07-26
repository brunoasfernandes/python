# Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode comprar
real = float(input('Quantos dinheiro você tem na carteira? R$ '))
dolar = real / 5.24
yuan = real / 0.76    # yuan chinês
iene = real / 0.040   # iene japonês
libra = real / 6.44   # reino unido
euro = real / 5.70
print('Com R${:.2f} você pode compar US${:.2f}, yuan{:.2f}, iene{:.2f}, libra{:.2f}, euro{}'.format(real, dolar, yuan, iene, libra, euro))
