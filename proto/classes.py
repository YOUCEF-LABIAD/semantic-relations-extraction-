#Definir une classe pour representer un noeud du graphe
class Node:
    def __init__(self, word):
        self.word = word
        #choix logique ici, 
            #un seul successeur pour eviter les erreurs?
            #plusieurs pour garder la flexibilite? (mots composes)
        self.successor = []  # Les noeuds suivants dans la sequence
        self.predecessor = []  # Les noeuds precedents dans la sequence
        #remplacer par une liste de relations?????
        self.relations =[]
        self.types ={}#[type possible : poids]




class relation:
    def __init__(self, idRel, typeRel, idMot1, idMot2):
        #type: par ex r_pos est identifiée globallement par "4"
        self.typeRel=typeRel
        #idRel: chaque isntance de relation?????
        self.idRel=idRel
        self.idMot1=idMot1
        self.idMot2=idMot2