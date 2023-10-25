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
            print("Você selecionou a opção 1.")
            break
        elif opcao2 == 2:
            print("Você selecionou a opção 2.")
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
            print("A ordem do grafo é: ",ordem)
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
            print("Você selecionou a opção 5.")
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
            print("Você selecionou a opção 9.")
            exibir_submenu()
            
        elif opcao == 10:
            print("Você selecionou a opção 10.")
            exibir_submenu()
            
        elif opcao == 11:
            print("Você selecionou a opção 11.")
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