
import networkx as nx
import matplotlib.pyplot as plt
from networkx import *
import os
import time

#Mini menu para retornar para o menu principal
def exibir_submenu():
    while True:
        print("\n----------//----------")
        print("Deseja voltar para o menu anterior?")
        print("1 - Sim")
        print("2 - Não (Sair do programa)")
        opcao = input("Digite uma opção: ")
        opcao = int(opcao)
        if opcao == 1:
            break
        elif opcao == 2:
            print("Saindo...")
            exit()
        else:
            print("Opção inválida.")


#Função para configurar a exibição do grafo
def configurarGrafo(Grafo_Generico):

    direciionado = nx.is_directed(Grafo_Generico)
    poderado = all('weight' in Grafo_Generico[u][v] for u, v in Grafo_Generico.edges())
    
    print("----------//----------\nDeseja que os vétices sejam numerados?")
    print("1 - Sim")
    print("2 - Não")
            
    numerados = int(input("Digite uma opção: "))
    if numerados == 1:
        valor = True     
    elif numerados == 2:
        valor = False
                
    print("----------//----------\nQual cor deseja que os vértices sejam?")
    print("1 - Azul")
    print("2 - Verde")
    print("3 - Vermelho")
    print("4 - Amarelo")
    print("5 - Preto")
    print("6 - Branco")
            
    cor_vertices = int(input("Digite uma opção: "))
    if cor_vertices == 1:
        cor_vertices = 'blue'
    elif cor_vertices == 2:
        cor_vertices = 'green'
    elif cor_vertices == 3:
        cor_vertices = 'red'
    elif cor_vertices == 4:
        cor_vertices = 'yellow'
    elif cor_vertices == 5:
        cor_vertices = 'black'
    elif cor_vertices == 6:
        cor_vertices = 'white'    
            
    print("----------//----------\nQual cor deseja que as arestas sejam?")
    print("1 - Azul")
    print("2 - Verde")
    print("3 - Vermelho")
    print("4 - Amarelo")
    print("5 - Preto")
    print("6 - Branco")
            
    cor_arestas = int(input("Digite uma opção: "))
    if cor_arestas == 1:
        cor_arestas = 'blue'
    elif cor_arestas == 2:
        cor_arestas = 'green'
    elif cor_arestas == 3:
        cor_arestas = 'red'
    elif cor_arestas == 4:
        cor_arestas = 'yellow'
    elif cor_arestas == 5:
        cor_arestas = 'black'
    elif cor_arestas == 6:
        cor_arestas = 'white'
        
    pos = nx.spring_layout(Grafo_Generico)    
        
    if direciionado == True:
        
        if poderado == True:
                # Desenha os vértices
                nx.draw_networkx_nodes(Grafo_Generico, pos, with_labels=valor, node_size=500, node_color=cor_vertices)
                
                # Desenha as arestas
                nx.draw_networkx_edges(Grafo_Generico, pos, edge_color=cor_arestas, width=2, arrows=True)
                
                # Desenha os pesos
                pesos = nx.get_edge_attributes(Grafo_Generico, 'weight')
                nx.draw_networkx_edge_labels(Grafo_Generico, pos, edge_labels=pesos)
                
                plt.show()
                
        # Desenha os vértices
        nx.draw_networkx_nodes(Grafo_Generico, pos, with_labels=valor, node_size=500, node_color=cor_vertices)
    
        # Desenha as arestas
        nx.draw_networkx_edges(Grafo_Generico, pos, edge_color=cor_arestas, width=2, arrows=True)  
        
        plt.show()
    
    else: 
        if poderado == True:
            # Desenha os vértices
            nx.draw_networkx_nodes(Grafo_Generico, pos, with_labels=valor, node_size=500, node_color=cor_vertices)
                
            # Desenha as arestas
            nx.draw_networkx_edges(Grafo_Generico, pos, edge_color=cor_arestas, width=2)
                
            # Desenha os pesos
            pesos = nx.get_edge_attributes(Grafo_Generico, 'weight')
            nx.draw_networkx_edge_labels(Grafo_Generico, pos, edge_labels=pesos)
                
            plt.show()
                
        nx.draw(Grafo_Generico, pos, with_labels=valor, font_weight='normal', node_size=500, node_color=cor_vertices, edge_color=cor_arestas)
        plt.show()


#receberGrafo()

Grafo = nx.Graph()
Grafo = nx.read_graphml('teste.graphml')   

#print("Digite o nome do arquivo que contém o grafo: ")
#Arquivo = input()
#Arquvo = str(Arquivo)
    
#A variável Grafo recebe um grafo lido de um arquivo GraphML (teste.graphml)
#Grafo = nx.read_graphml(Arquivo)
print("Grafo lido com sucesso!")

#Menu de opções
while True:
        #Continua a execução do programa até que o usuário digite a opção 14
        
        #Imprime o menu de opções
        print("\n\n/--------MENU--------/")
        print("01 - Imprimir grafo")
        print("02 - Retornar a ordem do grafo")
        print("03 - Retornar o tamanho do grafo")
        print("04 - Retornar os vizinhos de um vértice")
        print("05 - Determinar o grau de um vértice")
        print("06 - Retornar a sequência de graus do grafo")
        print("07 - Determinar a excentricidade de um vértice")
        print("08 - Determinar o raio do grafo")
        print("09 - Determinar o diâmetro do grafo")
        print("10 - Determinar o centro do grafo")
        print("11 - Determinar sequencia de vertices visitados na busca em largura")
        print("12 - Determinar distância e caminho mínimo")
        print("13 - Determinar a proximidade C de um vértice")
        print("14 - Sair")
        print("----------//----------")
        
        escolha = (input("Digite uma opção: "))
        escolha = int(escolha)
        
        #Imprime o grafo lido
        if escolha == 1:
            configurarGrafo(Grafo) #Mundança na função para grafos direcionados e com pesos
            exibir_submenu()
        
        #Retorna a ordem do grafo
        elif escolha == 2:
            ordem = Grafo.order()
            print("A ordem do grafo é: ", ordem)
            exibir_submenu()
            
        #Retorna o tamanho do grafo    
        elif escolha == 3:
            tamanho_grafo = len(Grafo.nodes()) + len(Grafo.edges())
            print("Tamanho do grafo", tamanho_grafo)
            exibir_submenu()
        
        #Retorna os vizinhos de um vértice        
        elif escolha == 4:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("Digite um vértice: ")
            vizinhos = list(Grafo.neighbors(vertice))
            print("Os vizinhos do vértice ", vertice, " são: ", vizinhos)
            exibir_submenu()
        
        #Determina o grau de um vértice        
        elif escolha == 5:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("Digite um vértice: ")
            grau = Grafo.degree(vertice)          
            print("O grau do vértice ", vertice, " é: ", grau)
            exibir_submenu()
        
        #Retorna a sequência de graus do grafo    
        elif escolha == 6:
            print("Você selecionou a opção 6.")
            print(Grafo.degree())
            exibir_submenu()
            
        #Determina a excentricidade de um vértice    
        elif escolha == 7:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("Digite um vértice: ")
            excentricidade = nx.eccentricity(Grafo, v=vertice, sp=None)
            print("A excentricidade do vértice ", vertice, " é: ", excentricidade)
            exibir_submenu()
        
        #Determina o raio do grafo    
        elif escolha == 8:
            raio = nx.radius(Grafo)
            print("O raio do grafo é:", raio)
            exibir_submenu()
        
        #Determina o diâmetro do grafo    
        elif escolha == 9:
            print("O diâmetro do grafo é: ", end='')
            diametro = diameter(Grafo)
            print(diametro)
            exibir_submenu()
            
        #Determina o centro do grafo    
	elif escolha == 10:
		print("Você selecionou a opção 10.")
		print(list(nx.center(G)))
		exibir_submenu()
        
        #Determina sequencia de vertices visitados na busca em largura    
        elif escolha == 11:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("Digite um vértice de início: ")
            sequencia = list(edge_bfs(Grafo, vertice))
            largura = nx.Graph()
            largura.add_edges_from(sequencia)
            visitados = [vertice]
            for aresta in sequencia:
                if aresta[0] not in visitados:
                    visitados.append(aresta[0])
                if aresta[1] not in visitados:
                    visitados.append(aresta[1])
            print("Sequência de vértices visitados:\n", visitados)
            isolados = []
            for aresta in Grafo.edges:
                if aresta not in largura.edges() and (aresta[1], aresta[0]) not in largura.edges():
                    isolados.append(aresta)
            if len(isolados)>0:
                print("Arestas que não fazem parte da busca em largura:")
                for aresta in isolados:
                    print(aresta, end=' ')
            else:
                print("Todas as arestas do grafo estão na árvore de busca em largura")
            nx.write_graphml(largura, "arvore_bfs.graphml")
            print("A árvore de busca em largura está salva em formato GraphML")
            print("Deseja exibir a árvore de busca em largura?")
            print("1 - Sim")
            print("2 - Não")
            exibir = int(input("Digite uma opção: "))
            if exibir == 1:
                configurarGrafo(largura)
            exibir_submenu()
            
        #Determina distância e caminho mínimo    
        elif escolha == 12:
            print("Você selecionou a opção 12.")
			v1=int(input("Digite o primeiro vertice desejado"))
			v2=int(input("Digite o segundo vertice desejado"))
			length, path = nx.bidirectional_dijkstra(Grafo, v1, v2)
			print("Distancia:")
			print(length)
			print("Caminho:")
			print(path)
            exibir_submenu()
        
        #Determina a proximidade C de um vértice    
        elif escolha == 13:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("De qual vertice gostaria de determinar a centralidade?\n")
            
            # Nao utilizando a funcao pronta
            # soma = 0
            # for no in list(Grafo.nodes):
            #    soma += nx.dijkstra_path_length(Grafo, source=vertice, target=no)
            # cent = (nx.number_of_nodes(Grafo) - 1)/soma
            # print(cent)

            # Utilizando a funcao pronta
            centralidade_proximidade_c = nx.closeness_centrality(Grafo, u=vertice, distance='weight')
            print("A centralidade de proximidade C do vertice", vertice, ": ", centralidade_proximidade_c)
            exibir_submenu()
        
        #Sai do programa    
        elif escolha == 14:
            print("Saindo...")
            break
        
        #Caso o usuário digite uma opção inválida
        else:
            print("Opção inválida.")
            print("Retornando ao menu principal...")
         
        #Tempo de espera para aparecer o menu principal novamente    
        time.sleep(1)
            print("Retornando ao menu principal...")
         
        #Tempo de espera para aparecer o menu principal novamente    
        time.sleep(1)
