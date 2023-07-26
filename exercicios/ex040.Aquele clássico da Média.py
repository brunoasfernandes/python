# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com sua média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Qual a sua nota da AV? '))
nota2 = float(input('Qual a sua nota da AVS? '))
media = (nota1 + nota2) / 2
print(f'''Nota AV: {nota1:.1f}
Nota AVS: {nota2:.1f}
Nota final: {media:.1f}''')

if media < 5:
    print('\033[7;31mREPROVADO. Até ano que vem! kkk\033[m')
elif media >= 7:
    print('\033[7;32mAPROVADO. Boas férias!\033[m')
else:
#elif media >= 5 and media < 7:
    print('\033[7;33mRECUPERAÇÃO. Precisa estudar mais!\033[m')



