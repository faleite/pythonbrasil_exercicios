"""
20. Altere o programa de cálculo do fatorial,
permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.
"""
qtd = int(input('Insira a quantidade de fatorial a ser calculado: '))

resultado = 1

for i in range(1, qtd + 1):
    while True:
        num = int(input(f'Insira o {i}º número: '))
        if 0 < num < 16:
            break
        else:
            print('Número inválido, digite novamente!')

    for n in range(1, num + 1):
        resultado *= n

    print(f'{num}! = {resultado}')
