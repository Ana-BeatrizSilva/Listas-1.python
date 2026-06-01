'''Em um sistema de e-commerce, não sabemos quantos itens o usuário vai 
comprar. A lista é a estrutura ideal para o "Carrinho". Crie um programa que: 1 
adicione elementos no carrinho, 2- tire elementos do carrinho, 3 - imprima 
elementos do carrinho e saia do programa. (Veja como se usa o match, case)'''

print('Bem-vindo!')
carrinho = []

while True:
    opcao = int(input('Escolha uma opção:\n' \
    '1 - Adicionar item\n' \
    '2 - Remover item\n' \
    '3 - Imprimir itens\n' \
    '4 - Sair\n' \
    ': '))

    match opcao:

        case 4:
            print('Saindo...')
            break

        case 1:
            print('Adicionar item')
            quantidade = int(input('Quantos itens deseja adicionar?: '))

            for i in range (quantidade):
                item = input('Digite o item que deseja adicionar: ')
                carrinho.append(item)
            
            print('Item adicionado!')

        case 2:
            print('Remover item')

            if carrinho:
                quantidade = int(input('Digite quantos itens deseja remover: '))

                for i in range (quantidade):
                    item = input('Digite os itens que deseja remover: ')
                    if item in carrinho:
                        carrinho.remove(item)
                        print('Item removido!')
                    else:
                        print('Item não encontrado')
        
        case 3:
            print('Imprimir carrinho')
            print(carrinho)