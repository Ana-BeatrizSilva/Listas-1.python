'''O laboratório de prototipagem precisa controlar as cores de filamentos PETG e 
ABS disponíveis para as cases de projetos IoT. Crie um sistema simples de 
inventário que: 
a. Inicie com uma lista de cores já disponíveis: ['Branco', 'Preto', 
'Azul']. 
b. Permita ao usuário digitar novas cores. 
c. Antes de adicionar, verifique se a cor já existe na lista (evitar duplicatas). 
d. Exiba a lista atualizada em ordem alfabética.'''

cores = ['Branco', 'Preto', 'Azul', 'Vermelho','Ciano']

while True:

    opcao = int(input('Deseja digitar novas cores?: \n'
    '1 - Sim\n'
    '2 - Não\n'
    ': '))

    match opcao:

        case 1:

            cor = input('Digite uma cor: ').strip().capitalize()
            if cor in cores:
                print('Cor não pode ser adicionada pois já existe na lista')
            else:
                cores.append(cor)
        
        case 2:
            break

cores.sort()
print(f'Lista em ordem alfabética: {cores}')