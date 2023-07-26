# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = float(input('Qual a distância da viagem em Km? '))
if viagem <= 200:
    passagem = viagem * 0.50
    print('\033[1;42mSua passagem vai ficar no valor de R$ {:.2f}\033[m'.format(passagem))
else:
    passagem = viagem * 0.45
    print('\0303[7;35mSua passagem ficou no valor de R$ {:.2f}\033[m'.format(passagem))

# if simplificado
'''distancia = float(input('Qual a distância da viagem? '))
passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Sua passagem vai ficar no valor de R$ {:.2f}'.format(passagem))'''




