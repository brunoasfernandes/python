# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu SEXO: [F/M] ')).strip().upper()[0]

while sexo not in 'F M':
    sexo = str(input('DADOS INVÁLIDOS. Por favor, informe seu SEXO: ')).strip().upper()[0]
print(f'Sexo informado: {sexo}')
