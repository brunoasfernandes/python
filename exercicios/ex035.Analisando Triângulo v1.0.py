# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[1;31m-=\033[m' * 15)
print('   \033[1;31mAnalisador de Triângulos\033[m')
print('\033[1;31m-=\033[m' * 15)

r1 = float(input('Primerio segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os elementos acima PODEM FORMAR um TRIÂNGULO')
else:
    print('Os elementos acima NÃO PODEM FORMAR um TRIÂNGULO')
