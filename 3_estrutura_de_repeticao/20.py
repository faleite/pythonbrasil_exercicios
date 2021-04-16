"""
20. Altere o programa de cálculo do fatorial,
permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.
"""
qtd = int(input('Insira a quantidade de fatorial a ser calculado: '))

for i in range(1, qtd + 1):
    while True:
        num = int(input(f'Insira o {i}º número: '))
        if 0 < num < 16:
            break
        else:
            print('Valor inválido. Digite novamente.')

    n = 1
    resultado = 1

    while n <= num:
        resultado *= n
        n += 1
    print(f'{num}! = {resultado}')
