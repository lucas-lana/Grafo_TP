import networkx as nx
#import matplotlib.pyplot as plt
from networkx import *
import os
import time

#Função para receber qualquer grafo.graphml

#def receberGrafo():
    # Cria um grafo vazio
#    Grafo = nx.Graph()
#    print("Digite o nome do arquivo que contém o grafo: ")
#    Arquivo = input()
#    Arquvo = str(Arquivo)
    
    #A variável Grafo recebe um grafo lido de um arquivo GraphML (teste.graphml)
#    Grafo = nx.read_graphml(Arquivo)
#    print("Grafo lido com sucesso!")


#Mini menu para retornar para o menu principal
def exibir_submenu():
    while True:
        print("\n----------//----------")
        print("Deseja voltar para o menu anterior?")
        print("1 - Sim")
        print("2 - Não")
        opcao2 = input("Digite uma opção: ")
        opcao2 = int(opcao2)
        if opcao2 == 1:
            break
        elif opcao2 == 2:
            exit()
        else:
            print("Opção inválida.")


#receberGrafo()

Grafo = nx.Graph()
Grafo = nx.read_graphml('teste.graphml')   
print("Grafo lido com sucesso!")

#Menu de opções
while True:
        #Continua a execução do programa até que o usuário digite a opção 14
        
        #Imprime o menu de opções
        print("\n\n----MENU----\n")
        print("1 - Imprimir grafo")
        print("2 - Retornar a ordem do grafo")
        print("3 - Retornar o tamanho do grafo")
        print("4 - Retornar os vizinhos de um vértice")
        print("5 - Determinar o grau de um vértice")
        print("6 - Retornar a sequência de graus do grafo")
        print("7 - Determinar a excentricidade de um vértice")
        print("8 - Determinar o raio do grafo")
        print("9 - Determinar o diâmetro do grafo")
        print("10 - Determinar o centro do grafo")
        print("11 - Determinar sequencia de vertices visitados na busca em largura")
        print("12 - Determinar distância e caminho mínimo")
        print("13 - Determinar a proximidade C de um vértice")
        print("14 - Sair")
        print("----------//----------")
        
        
        opcao = (input("\nDigite uma opção: "))
        opcao = int(opcao)
        
        if opcao == 1:
            #nx.draw(Grafo, with_labels=True, font_weight='bold')
            print("Em desenvolvimento...")
            exibir_submenu()
        
        elif opcao == 2:
            ordem = Grafo.order()
            print("A ordem do grafo é: ", ordem)
            exibir_submenu()
            
        elif opcao == 3:
            print("Você selecionou a opção 3.")
            exibir_submenu()
                
        elif opcao == 4:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("Digite um vértice: ")
            vizinhos = list(Grafo.neighbors(vertice))
            print("Os vizinhos do vértice ", vertice, " são: ", vizinhos)
            exibir_submenu()
                
        elif opcao == 5:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("Digite um vértice: ")
            grau = Grafo.degree(vertice)          
            print("O grau do vértice ", vertice, " é: ", grau)
            exibir_submenu()
            
        elif opcao == 6:
            print("Você selecionou a opção 6.")
            exibir_submenu()
            
        elif opcao == 7:
            print ("Vértices do grafo: ", Grafo.nodes())
            vertice = input("Digite um vértice: ")
            excentricidade = nx.eccentricity(Grafo, v=vertice, sp=None)
            print("A excentricidade do vértice ", vertice, " é: ", excentricidade)
            exibir_submenu()
            
        elif opcao == 8:
            print("Você selecionou a opção 8.")
            exibir_submenu()
            
        elif opcao == 9:
            print("O diâmetro do grafo é: ", end='')
            diametro = diameter(Grafo)
            print(diametro)
            exibir_submenu()
            
        elif opcao == 10:
            print("Você selecionou a opção 10.")
            exibir_submenu()
            
        elif opcao == 11: #BÁRBARA:
            # Determinar a sequência de vértices visitados na busca em largura e informar a(s)
            # aresta(s) que não faz(em) parte da árvore de busca em largura. OBS: a árvore de
            # largura deve ser gerada também em formato GraphML.
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
            exibir_submenu()
            
        elif opcao == 12:
            print("Você selecionou a opção 12.")
            exibir_submenu()
            
        elif opcao == 13:
            print("Você selecionou a opção 13.")
            exibir_submenu()
            
        elif opcao == 14:
            print("Você selecionou a opção 14.")
            break
        else:
            print("Opção inválida.")
            
        time.sleep(1)