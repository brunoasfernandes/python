# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()  # .strip() para tirar os espaços antes e depois, .upper() para converter para o maiúsculo
palavras = frase.split()   # .split() usado para separar a frase em palavras
junto = '' .join(palavras)  # .join() usado para juntar as palavras sem espaço
inverso = ''

# inverso = junto[::-1]    jeito simplificado sem usar o laço for

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'Temos um palíndromo!')
    print(f'O inverso de {junto} é {inverso}')
else:
    print('A frase NÃO É um palíndromo!')




