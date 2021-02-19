"""5. Faça um Programa que converta metros para centímetros."""

metros = float(input('Insira a metragem: '))
centimetros = metros / 0.010000  # outra forma: metros * 100
print(f'{metros:.2f}m = {centimetros:.2f}cm')
