# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
# Equilátero: Todos os lados iguais.
# Isósceles: Dois lados iguais.
# Escaleno: Todos os lados diferentes.

lado1 = float(input('Digite um segmento de reta em CM: '))
lado2 = float(input('Digite outro segmento de reta em CM: '))
lado3 = float(input('Digite mais um segmento de reta em CM: '))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 == lado3:
        print('Esses segmentos PODEM forma um TRIÂNGULO do tipo EQUILÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print('Esses segmentos PODEM forma um TRIÂNGULO do tipo ESCALENO.')
    else:
        print('Esses segmentos PODEM forma um TRIÂNGULO do tipo ISÓSCELES')
else:
    print('Esses segmentos NÃO PODEM forma um TRIÂNGULO.')
