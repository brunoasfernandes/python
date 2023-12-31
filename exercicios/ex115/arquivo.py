from ex115.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # leitura do arquivo
        a.close()  # fecha arquivo
    except FileNotFoundError:  # se arquivo não encontrado
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # criar arquivo
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastra(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # ("a" de append) abrindo o arquivo para colocar dados
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # (write) para escrever no arquivo
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
