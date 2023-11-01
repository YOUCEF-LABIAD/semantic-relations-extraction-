from classes import Node


#Fonction pour creer le graphe a partir d'une phrase
def create_graph(text):
    words = text.split()  # Separez le texte en mots
    startNode = Node("START")  # Liste de noeuds representant le graphe
    endNode = Node("END")
    
    # Creez un noeud pour chaque mot dans le texte
    graph = [startNode]
    for word in words:
        node = Node(word)
        #TODO:node.types=Node.getTypes()
        graph.append(node)
    graph.append(endNode)

    # Connectez les noeuds avec la relation "r_succ"
    for i in range(len(graph) - 1):
        graph[i].successor.append(graph[i + 1])
        graph[i + 1].predecessor.append(graph[i])

    return graph

#ajouter les mots composes trouves au graphe de la phrase lue
def addComposedWords(graph):
    #TODO
    return 1

#Fonction pour afficher le graphe
def print_graph(graph):
    for node in graph:
        successor = ", ".join([succ.word for succ in node.successor])
        print(f"{node.word} -> [{successor}]")




#Exemple d'utilisation
text = "le petit chat boit du lait de chevre"
graph = create_graph(text)
print_graph(graph)