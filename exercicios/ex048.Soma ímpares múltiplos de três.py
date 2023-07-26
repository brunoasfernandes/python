# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# como ele fez
soma = 0
cont = 0
for c in range(1, 501, 2):  # pulando de 2 em 2 para pra achar os números ímpares
    if c % 3 == 0:          # achando os números que são múltiplos de três
        cont += 1     # achando quantos valores tem
        soma += c     # somando os valores ímpares e que são múltiplos de três
print('A soma dos {} valores solicitados é {}'.format(cont, soma))


# como eu fiz
soma = 0
cont = 0
for c in range(1, 500+1):
    if c % 3 == 0:                 # achando os números que são múltiplos de três
        if c % 2 != 0:             # achando números ímpares
            cont = cont + 1        # achando  quantos valores tem
            soma = soma + c        # somando os valores ímpares e que são múltiplos de três
print(f'A soma dos {cont} valores solicitados é {soma}')
