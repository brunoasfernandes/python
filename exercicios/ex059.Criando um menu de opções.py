from time import sleep

primeiro = float(input('Primeiro valor: '))
segundo = float(input('Segundo valor: '))
opções = soma = multiplicar = maior = 0

while opções != 5:
    print('~' * 20)
    print('''[1] Somar
[2] Multiplicar     
[3] Maior           
[4] Novos valores   
[5] Sair do programa''')
    print('~' * 20)
    opções = int(input('Escolha uma opção: '))
    if opções == 1:
        soma = primeiro + segundo
        print(f'A soma dos valores é: {soma}')
    elif opções == 2:
        multiplicar = primeiro * segundo
        print(f'A multiplicação dos valores é: {multiplicar}')
    elif opções == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print(f'Dos valores digitados o maior é {maior}')
    elif opções == 4:
        primeiro = float(input('Primeiro valor: '))
        segundo = float(input('Segundo valor: '))
    elif opções == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('\033[31mERRO!\033[m Escolha uma opção valida!')
print('Fim do programa.')
