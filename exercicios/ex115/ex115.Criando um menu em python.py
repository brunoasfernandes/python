from time import sleep
from ex115.interface import *
from ex115.arquivo import *
arq = 'ex115.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastra nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # opção de ler o arquivo
        lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        # opção de cadastra uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().upper()
        idade = leiaInt('Idade: ')
        cadastra(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        sleep(2)
        print('Até logo!')

        break
    else:
        print('\033[31mERRO: Opção inválida!\033[m')
