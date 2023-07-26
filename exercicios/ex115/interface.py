def leiaInt(msg):
    while True:
        try:  # tente fazer isso
            n = int(input(msg))
        except(ValueError, TypeError):  # se der problema, faça isso
            print('\033[31mERRO! Digite um numero inteiro!\033[m')
            continue
        except KeyboardInterrupt:  # se o programa for interrompido
            print('Entrada de dados interrompida')
            return 0
        else:
            return n


def linha(tam=50):
    print('-' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(50))
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c} - {item}\033[m')
        c += 1
    linha()
    opção = leiaInt('Sua opção: ')
    return opção
