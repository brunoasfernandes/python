numero = int(input('Digite um número para\ncalcular seu fatorial: '))
cont = numero
fatorial = 1

print(f'Calculando {numero}!')
for cont in range(numero, 0, -1):
    print(cont, end=' ')
    print('x' if cont > 1 else '=', end=' ')
    fatorial = fatorial * cont
print(fatorial)
