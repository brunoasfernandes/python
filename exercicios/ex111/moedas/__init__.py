def aumentar(valor=0, taxa=0, format=False):
    valor += valor * taxa / 100
    return moeda(valor) if format else valor


def reduzir(valor=0, taxa=0, format=False):
    valor -= valor * taxa / 100
    return moeda(valor) if format else valor


def dobro(valor=0, format=False):
    valor = valor * 2
    return valor if not format else moeda(valor)


def metade(valor=0, format=False):
    valor = valor / 2
    return valor if not format else moeda(valor)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aumen=0, reduz=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analizado: \t{moeda(valor)}')
    print(f'Dobro do valor:  \t{dobro(valor, True)}')
    print(f'Metade do valor: \t{metade(valor, True)}')
    print(f'{aumen}% de aumento: \t{aumentar(valor, aumen, True)}')
    print(f'{reduz}% de redução: \t{reduzir(valor, reduz, True)}')
    print('-' * 30)

