# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
import random
from typing import List
from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem de apresentação será:")
print(lista)