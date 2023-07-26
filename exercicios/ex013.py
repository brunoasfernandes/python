# Faça um algoritimo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.
salário = float(input('Qual o seu salário atual? R$'))
novo_salário = salário + (salário * 15/100)
print('Você recebeu 15% de aumento, parabéns o seu novo salário é de R${:.2f}!'.format(novo_salário))
