import networkx as nx

# Cria um grafo vazio
Grafo = nx.Graph()

#A variável Grafo recebe um grafo lido de um arquivo GraphML (teste.graphml)
Grafo = nx.read_graphml('teste.graphml')


#Menu de opções
while True:
    #Continua a execução do programa até que o usuário digite a opção 14
    
    #Imprime o menu de opções
    print("\n\n----MENU----\n")
    print("\n1 - Adicionar nó")
    print("2 - Adicionar aresta")
    print("3 - Imprimir grafo")
    print("4 - Retornar a ordem do grafo")
    print("5 - Retornar o tamanho do grafo")
    print("6 - Retornar os vizinhos de um vértice")
    print("7 - Determinar o grau de um vértice")
    print("8 - Retornar a sequência de graus do grafo")
    print("9 - Determinar a excentricidade de um vértice")
    print("10 - Determinar o raio do grafo")
    print("11 - Determinar o diâmetro do grafo")
    print("12 - Determinar o centro do grafo")
    print("13 - Determinar sequencia de vertices visitados na busca em largura")
    print("14 - Determinar distância e caminho mínimo")
    print("15 - Determinar a proximidade C de um vértice")
    print("16 - Sair")
    print("----------//----------")
    
    
    opcao = int(input("Digite uma opção: "))
    
    
    #Estrutura de switch case
    def case1():
        print("Você selecionou a opção 1.")

    def case2():
        print("Você selecionou a opção 2.")

    def case3():
        print("Você selecionou a opção 3.")

    def case4():
        print("Você selecionou a opção 4.")

    def case5():
        print("Você selecionou a opção 5.")

    def case6():
        print("Você selecionou a opção 6.")

    def case7():
        print("Você selecionou a opção 7.")

    def case8():
        print("Você selecionou a opção 8.")

    def case9():
        print("Você selecionou a opção 9.")

    def case10():
        print("Você selecionou a opção 10.")

    def case11():
        print("Você selecionou a opção 11.")

    def case12():
        print("Você selecionou a opção 12.")

    def case13():
        print("Você selecionou a opção 13.")
        
    def case14():
        print("Você selecionou a opção 14.")
    
    def case15():
        print("Você selecionou a opção 15.")
    
    def case16():
        print("Você selecionou a opção 16.")
        break
        
    def case_default():
        print("Opção inválida.")
        break

    switch_case = {
        1: case1, 2: case2, 3: case3,
        4: case4, 5: case5, 6: case6,
        7: case7, 8: case8, 9: case9,
        10: case10, 11: case11, 12: case12, 13: case13,
        14: case14, 15: case15,16: case16
    }
