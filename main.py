#Dicionario para armazenar os produtos e suas quantidades
estoque = {}

#função para adicionar produtos ao estoque
def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip().lower() #.strip e .lower() para remover espaços e padronizar o nome
    quantidade = input("Digite a quantidade do produto: ").strip()
    #Validação de entrada
    if not nome:
        print("O nome do produto não pode ser vazio.")
        return
        #Validação para garantir que a quantidade seja um número inteiro positivo
    if not quantidade.isdigit() or int(quantidade) < 0: #isdigit() verifica se a string é composta apenas por dígitos, inteiros e positivos 
        print("ERRO: A quantidade deve ser um número inteiro positivo.")    
        return
    estoque[nome] = int(quantidade) #adiciona o produto e a quantidade ao dicionário estoque
    print(f"O produto {nome} com quantidade {quantidade} foi adicionado ao estoque.") 
#função para listar produtos no estoque
def listar_produtos():
    print("produtos em estoques: ")
    #for para percorrer o dicionário estoque e imprimir os produtos e suas quantidades
    for nome, quantidade in estoque.items(): #.items() retorna uma lista de tuplas contendo os pares chave-valor do dicionário
        print(f"- {nome}: {quantidade}")
    #Verifica se o estoque está vazio e exibe uma mensagem apropriada
    if not estoque:
        print("Nenhum produto no estoque.") 
    
#função para atualizar produtos no estoque
def atualizar_produto():
    #Solicitar ao usuário o nome do produto que vai ser atualizado
    nome = input("Digite o nome do produto que vai ser atualizado: ").strip().lower()
    if nome in estoque:
        #Solicitar ao usuário a nova quantidade do produto
        quantidade = input("Digite a nova quantidade do produto: ").strip()
        #Validação para garantir que a quantidade seja um número inteiro positivo
        if not quantidade.isdigit() or int(quantidade) < 0:
            print("ERRO: A quantidade deve ser um número inteiro positivo.")
            return
        estoque[nome] = int(quantidade) #atualiza a quantidade do produto no dicionário estoque
        print(f"O produto {nome} foi atualizado para {quantidade} unidades.")
    else:
        print("produto não encontrado no estoque.")
#função para remover produtos do estoque
def remover_produto():
    nome = input("Digite o nome do produto que vai ser removido: ").strip().lower()
    #Validação para garantir que o produto exista no estoque antes de removê-lo
    if nome in estoque:
        #remove o produto do dicionario usando a função del
        del estoque[nome]
        print(f"O produto {nome} foi removido do estoque.")
    else:
        print("produto não encontrado.")

#função para exibir o menu e lidar com as opções do usuário
def menu():
    #loop infinito para exibir o menu até que o usuário escolha sair
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Sair")
        #Solicita ao usuário que escolha uma opção do menu
        escolha = input("Escolha uma opção: ")
        #direciona o fluxo do programa para a função correspondente à escolha do usuário
        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            remover_produto()
        elif escolha == "5":
            print("Saindo...")
            break #encerra o loop e sai do programa
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__": #verifica se o script está sendo executado diretamente e não importado como módulo
    menu()
