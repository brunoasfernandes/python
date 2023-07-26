def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[;31mERRO: "{entrada}" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        try:    # tente fazer isso
            n = int(input(msg))
        except(ValueError, TypeError):  # se der problema, faça isso
            print('\033[31mERRO! Digite um numero inteiro!\033[m')
            continue
        except KeyboardInterrupt:   # se o programa for interrompido
            print('Entrada de dados interrompida')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:    # tente fazer isso
            n = float(input(msg))
        except(ValueError, TypeError):  # se der problema, faça isso
            print('\033[31mERRO! Digite um numero inteiro!\033[m')
            continue
        except KeyboardInterrupt:   # se o programa for interrompido
            print('Entrada de dados interrompida')
            return 0
        else:
            return n


