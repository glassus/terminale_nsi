```python linenums='1' hl_lines='14 16 18 19 21'
class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle) 

```