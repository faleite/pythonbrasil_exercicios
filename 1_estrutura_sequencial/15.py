"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor = float(input('Insira o valor por hora de trabalho: '))
horas = float(input('Insira o número de horas trabalhadas no mês: '))
s_bruto = valor * horas
ir = s_bruto * 0.11
inss = s_bruto * 0.08
sind = s_bruto * 0.05
sal_liq = s_bruto - (ir + inss + sind)
print(f'Salário Bruto: R$ {s_bruto:.2f}')
print(f'IR (11%): R$ {ir:.2f}')
print(f'INSS (8%): R$ {inss:.2f}')
print(f'Sindicato (5%): R$ {sind:.2f}')
print(f'Salário Liquido: R$ {sal_liq:.2f}')
