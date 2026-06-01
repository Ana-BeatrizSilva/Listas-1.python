'''No desenvolvimento de um protótipo de Bengala Inteligente com sensores 
ultrassônicos, é comum receber leituras inválidas (ruído). Considere uma lista 
de distâncias capturadas em centímetros. Escreva um programa que receba 
uma lista de leituras. O programa deve: 
a. Remover leituras menores que 2 cm ou maiores que 400 cm (limites do 
sensor HC-SR04). 
b. Calcular a média das leituras válidas usando a fórmula: 
c. Exibir a lista "limpa" e a média final.'''

lista = [2, 40, 650, 3, 4, 5, 420, 3, 10, 530]
lista_limpa = []

for i in lista:
    if i >= 2 and i <= 400:
        lista_limpa.append(i)

print(f'Lista limpa: {lista_limpa}')
print(f'Média: {sum(lista_limpa)/len(lista_limpa)}')