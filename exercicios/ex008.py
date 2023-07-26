# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
medida = float(input('Uma distância em metros! '))
cm = medida * 100
mm = medida * 1000
print('{} metros é igual a: {:.0f}cm \nQue é igual a: {:.0f}mm'.format(medida, cm, mm))






