'''Faça um programa que gere uma lista contendo somente “Aprovados” ou 
“reprovados”, de acordo com as médias da lista notas = [4, 7, 9, 5, 8], sabendo 
que médias acima de 6,9 são aprovados, senão reprovados. '''

notas = [4, 7, 9, 5, 8]
lista = []

for i in notas:
    if i > 6.9:
        lista.append('Aprovado')
    else:
        lista.append('Reprovado')

print(lista)