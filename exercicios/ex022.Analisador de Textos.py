# Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas, o nome com todas minúsculas.
# quantas letras ao (sem considerar os espaços).
# e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {} letra'.format(len(nome) - nome.count(' ')))
# print('seu primeiro nome tem: {} letra'.format(nome.find(' ')))
nome1 = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome1[0], len(nome1[0])))


