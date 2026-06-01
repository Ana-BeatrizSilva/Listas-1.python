'''Monitorando a rede elétrica do rack de servidores, o sistema registrou 
flutuações de tensão ao longo de 10 minutos. Dada uma lista de tensões, por 
exemplo: [218, 220, 224, 230, 221, 190, 220, 235]. 
a. Identifique e exiba a maior e a menor tensão registrada. 
b. Crie uma nova lista chamada anomalias que contenha apenas as 
tensões que estejam fora da faixa ideal (entre 210V e 230V). 
c. Se a lista de anomalias não estiver vazia, exiba um alerta de 
"Manutenção Necessária".'''

tensoes =  [218, 220, 224, 230, 221, 190, 220, 235]

print(f'Maior tensão: {max(tensoes)}')
print(f'Menor tensão: {min(tensoes)}')

anomalias = []

for i in tensoes:
    if i > 230 or i < 210:
        anomalias.append(i)

print(f'Anomalias: {anomalias}')
print(f'Quantidade de anomalias: {len(anomalias)}')
if len(anomalias) > 0:
    print('Manutenção necessária')