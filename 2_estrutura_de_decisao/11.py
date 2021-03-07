""" 11. As Organizações Tabajara resolveram dar um aumento de salário
aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
"""

salario = float(input(f'Insira o salário atual: '))

aumento = 0

if salario <= 280.00:
    aumento = 20
elif 280.00 < salario <= 700.00:
    aumento = 15
elif 700.00 < salario <= 1500.00:
    aumento = 10
else:
    aumento = 5

print(f'Salário antes do reajuste: R$ {salario:.2f}')
print(f'Percentual de aumento aplicado: {aumento}%')
print(f'Valor do aumento: R$ {salario * aumento / 100:.2f}')
print(f'Novo salário, após o aumento: R$ {(salario * aumento / 100) + salario:.2f}')
