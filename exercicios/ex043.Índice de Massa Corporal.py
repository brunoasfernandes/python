# Desenvolva uma lógica que que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu etatus de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# De 25 até 30: Acima do peso
# De 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
peso = float(input('Digite seu peso (KG): '))
altura = float(input('Qual é a sua altura (M): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu índice de massa corpórea é {imc:.2f}: Está abaixo do ideal.')
elif 18.5 <= imc < 25:
    print(f'Seu índice de massa corpórea é {imc:.2f}: Está ideal!')
elif imc <= 30:
    print (f'Seu índice de massa corpórea é {imc:.2f}: Você está com sobre peso!')
elif imc <= 40:
    print(f'Seu índice de massa corpórea é {imc:.2f}: Você está obeso!')
else:
    print(f'Seu índice de massa corpórea é {imc:.2f}: Você é um obeso mórbido!')
