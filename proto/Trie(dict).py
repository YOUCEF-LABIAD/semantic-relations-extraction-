class Trie(object):
    def __init__(self,wd="",end=False):
        self.br={}; self.end=end
        if wd!="": self.addword(wd)
    def __repr__(self): # Uniquement pour les tests
        br=self.br.__repr__()
        m='E,' if self.end else ""
        return "T["+m+br+"]"

#On peut creer un Trie vide : z=Trie(), ou forcer tout de suite son initialisation avec un mot : z=Trie('unMot').

    def addword(self,wd):
        br=self.br
        if wd:
            c=wd[0]; rst=wd[1:] # Decoupage essentiel
            if c not in br: br[c]=Trie() # Nouvelle branche
            br[c].addword(rst)
        else: self.end=True # Marqueur de la fin       
    def __getitem__(self,c):  # Objet emule une liste/dict.
        return self.br[c]