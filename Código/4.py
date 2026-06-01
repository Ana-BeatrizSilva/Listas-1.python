'''Imagine que você está monitorando a temperatura de sensores. Precisamos 
armazenar as leituras para gerar um relatório de picos. Considere as leituras de 
temperatura coletadas a cada hora: leituras_temp = [22.5, 23.0, 25.8, 24.2, 28.5, 21.9]. Gere um programa que mostre a maior, a menor e a média de 
temperaturas.'''

leituras_temp = [22.5, 23.0, 25.8, 24.2, 28.5, 21.9]

print(f'Maior temperatura: {max(leituras_temp)}')
print(f'Menor temperatura: {min(leituras_temp)}')
print(f'Média de temperaturas: {sum(leituras_temp)/len(leituras_temp)}')