"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                    Até 5 Kg            Acima de 5 Kg
Morango         R$ 2,50 por Kg         R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg         R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
e escreva o valor a ser pago pelo cliente.
"""

qte_mor = float(input('Insira a quantidade em Kg de Morangos: '))
qte_mac = float(input('Insira a quantidade em Kg de Maças: '))

if qte_mor and qte_mac <= 5:
    valor_morango = qte_mor * 2.50
    valor_maca = qte_mac * 1.80
else:
    valor_morango = qte_mor * 2.20
    valor_maca = qte_mac * 1.50

valor_total = valor_morango + valor_maca
peso_total = qte_mor + qte_mac

if peso_total > 8 or valor_total > 25:
    valor_total = valor_total - (valor_total * 10 / 100)

print(f'Valor total a pagar: R$ {valor_total:.2f}')
