# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade do carro em Km/h? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Multado! Você exedeu o limite de 80Km/h')
    print('Sua multa é de {:.2f} R$'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Tenha um bom dia! Você está dentro do limite de velocidade!')
