# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número para calcular seu fatorial: '))
cont = numero
fatorial = 1

print(f'Calculando o {numero}!')
while cont > 0:
    print(cont, end=' ')
    print('X' if cont > 1 else '=', end=' ')
    fatorial = fatorial * cont
    cont = cont - 1
print(fatorial)
