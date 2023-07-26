# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao      # formula de calculo do décimo termo de uma PA
for c in range(primeiro, decimo + 1, razao):
    print(c, end=', ')
print('FIM')

