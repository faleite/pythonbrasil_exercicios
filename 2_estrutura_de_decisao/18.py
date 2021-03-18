"""
18. Faça um Programa que peça uma data no formato
dd/mm/aaaa e determine se a mesma é uma data válida.
"""

data = input(f'Insira uma data no formato dd/mm/aaaa: ')

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

if 0 < dia <= 31:
    if 0 < mes <= 12:
        if ano > 0:
            print('Data válida.')
        else:
            print('Data inválida.')
    else:
        print('Data inválida.')
else:
    print('Data inválida.')
