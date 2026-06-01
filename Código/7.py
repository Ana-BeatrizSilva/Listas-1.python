'''Em um evento como o CONEDU, a organização precisa processar a lista de 
presença para emitir certificados. Você recebeu uma lista bruta com nomes de 
alunos que passaram pelo sensor de RFID na entrada, mas alguns nomes estão 
repetidos porque o aluno passou mais de uma vez. 
Exemplo de entrada: ['Ana', 'Bruno', 'Ana', 'Carlos', 'Bruno', 
'Daniel'] 
a. Gere uma nova lista contendo apenas nomes únicos. 
b. Conte quantos alunos distintos compareceram. 
c. Verifique se um nome específico (digitado pelo professor) está na lista de 
presença.'''

alunos =  ['Ana', 'Bruno', 'Ana', 'Carlos', 'Bruno', 'Daniel', 'Letícia', 'Bruno', 'Carlos', 'Maria', 'Luana','Alice','Mateus'] 

lista = []

for i in alunos:
    if i not in lista:
        lista.append(i)

print(f'Alunos distintos: {lista}')
print(f'Número de alunos distintos: {len(lista)}')

nome = input('Digite um nome para verificar se está na lista: ').strip().capitalize()

if nome in lista:
    print('Está na lista de presença')
else:
    print('Não está na lista de presença')