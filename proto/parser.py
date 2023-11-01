# Fonction pour lire un fichier en omettant les lignes "//" et vides
def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Supprimer les espaces en debut et fin de ligne
                line = line.strip()
                # Ignorer les lignes vides
                if not line:
                    continue
                # Ignorer les lignes commencant par "//"
                if line.startswith("//"):
                    continue
                # Traitement specifique a ajouter ici
                addComposedWord(line)
                # Par exemple, vous pouvez imprimer les lignes restantes
                print(line)
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' n'a pas ete trouve.")

# fonction qui ajoute un mot compose au bon trie
def addComposedWord(line):
    #decomposer le mot
    words = line.split()
    #chercher ou creer le fichier correspondant au premier mot
    first_word = words.pop(0) 
    file_name = first_word + "_composed_terms.pickle"
    #si le fichier existe on cree une nouvelle branche?????
        #on doit eviter de creer une nouvelle branche si on a un chemin qui existe deja (pompe a velo, pompe a eau ::: "pompe a" est un chemin commun entre les deux mots compo)
    if file_name exists:
        with open(file_name, 'rb') as trie:
        loaded_data = pickle.load(trie)
        current_word = trie
        for each w in words:
            if #prochain mot existe dans successeurs passer a l'etape suivante
            current_word.successors.append(w)
            current_word = w

    else create and add




# Exemple d'utilisation
file_path = 'termesCompSample.txt'  # Remplacez par le chemin de votre fichier
parse_file(file_path)