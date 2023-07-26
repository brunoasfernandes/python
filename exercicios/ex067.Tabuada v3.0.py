# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Digite um valor para ver sua tabuada ou número negativo p/ sair: '))
    print('-' * 15)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c}  = {num * c}')
    print('-' * 15)
print('<< Programa Tabuada Encerrado >>')
