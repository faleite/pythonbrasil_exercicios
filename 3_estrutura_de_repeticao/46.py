"""
46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
em seus saltos e depois informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos.
Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve
ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m
Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

while True:
    saltos = []
    atleta = str(input('Atleta: '))
    if atleta == '':
        break
    for s in range(1, 6):
        salto = float(input(f'Informe o {s}º Salto: '))
        saltos.append(salto)
    print()
    print(f'Atleta: {atleta}')
    print(f'Primeiro Salto: {saltos[0]} m')
    print(f'Segundo Salto: {saltos[1]} m')
    print(f'Terceiro Salto: {saltos[2]} m')
    print(f'Quarto Salto: {saltos[3]} m')
    print(f'Quinto Salto: {saltos[4]} m')

    saltos.sort()
    maior = saltos[-1]
    menor = saltos[0]
    saltos = saltos[1:4]  # O mesmo que saltos[1:-1]

    media = sum(saltos) / 3

    # Outra forma para extrair maior, menor e média

    # maior = menor = lst[0]
    #
    # for valor in lst:
    #     if valor > maior:
    #         maior = valor
    #     if valor < menor:
    #         menor = valor
    # lst.remove(maior)
    # lst.remove(menor)

    # media = sum(lst) / 3

    print(f'Melhor salto: {maior} m')
    print(f'Pior salto: {menor} m')
    print(f'Média dos demais saltos: {media:.2f} m')
    print('Resultado final:')
    print(f'{atleta}: {media:.2f} m')
    print()
