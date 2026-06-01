'''Faça um programa que gere uma lista que dá 10% de desconto para quem custa 
mais de 100, mas ignora itens que custam menos de 10. Considere a lista 
precos = [10, 50, 150, 200, 5] como referência.'''

precos = [10, 50, 150, 200, 5]
descontos = []

for preco in precos:
    if preco < 10:
        continue
    elif preco > 100:
        descontos.append(preco*0.9)
    else:
        descontos.append(preco)

print(descontos)