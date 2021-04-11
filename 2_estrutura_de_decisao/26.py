"""
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
- Álcool:
a. até 20 litros, desconto de 3% por litro
b. acima de 20 litros, desconto de 5% por litro
- Gasolina:
a. até 20 litros, desconto de 4% por litro
b. acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma:
A-álcool, G- gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

tipo = str(input('Insira o tipo de combustível (A-álcool, G- gasolina): ')).upper()
qtde = float(input('Insira a quantidade em litros: '))

alcool = qtde * 1.90
gasolina = qtde * 2.50
valor = 0

if tipo == 'A' and qtde <= 20:
    valor = alcool - (alcool * 3 / 100)
    print(f'Valor a ser pago: R$ {valor:.2f}')
elif tipo == 'A' and qtde > 20:
    valor = alcool - (alcool * 5 / 100)
    print(f'Valor a ser pago: R$ {valor:.2f}')
else:
    if tipo == 'G' and qtde <= 20:
        valor = gasolina - (gasolina * 4 / 100)
        print(f'Valor a ser pago: R$ {valor:.2f}')
    elif tipo == 'G' and qtde > 20:
        valor = gasolina - (gasolina * 6 / 100)
        print(f'Valor a ser pago: R$ {valor:.2f}')
    else:
        print('Tipo inválido')
