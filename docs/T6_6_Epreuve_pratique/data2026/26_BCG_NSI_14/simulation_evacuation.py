from random import randint, shuffle
from copy import deepcopy


class Piece:

    def __init__(self, profondeur: int, largeur: int):
        self.grille = [[0 for _ in range(largeur)] for _ in range(profondeur)]
        self.i_max = profondeur-1
        self.j_max = largeur-1
        self.capacite = profondeur * largeur * 5
        self.sorties = []

    def ajouter_occupants(self, i: int, j: int, nb: int):
        ''' permet d'ajouter jusqu'à nb occupants dans la case située ligne i et colonne j.
            Le nombre d'occupants ajoutés est limité par la capacité d'accueil de la case (5).
            Cette méthode renvoie le nombre d'occupants effectivement ajoutés.
        '''
        nb_add = min(nb, 5 - self.grille[i][j])
        if nb_add > 0:
            self.grille[i][j] = self.grille[i][j] + nb_add
        return nb_add

    def nb_occupants_restants(self) -> int:
        ''' renvoie le nombre d'occupants restants dans la pièce.
            A FAIRE EN PARTIE 1
        '''
        pass

    def ajouter_sortie(self, direction: str, position: int):
        ''' permet d'ajouter des sorties à la pièce.
            A COMPLETER EN PARTIE 2 (Pour l'instant, on n'utilise que deux directions !)
        '''
        if direction == "N":
            self.sorties.append((0, position))
        elif direction == "O":
            self.sorties.append((position, 0))

    def choix_sortie(self, i: int, j: int) -> tuple:
        ''' renvoie la sortie à utiliser pour une personne positionnée sur la ligne i et la colonne j.
            A CORRIGER EN PARTIE 2 (Pour l'instant, seule la 1ère sortie est utilisée !)
        '''
        def distance_de_manhattan(destination):
            ''' fonction privée renvoyant la distance de Manhattan entre la case (i,j) et la destination reçue en paramètre.
            '''
            return abs(i - destination[0]) + abs(j - destination[1])
        assert len(self.sorties) > 0, "Aucune sortie"
        choix = self.sorties[0]
        distance = distance_de_manhattan(choix)
        for k in range(1, len(self.sorties)):
            autre_sortie = self.sorties[k]
            if k < 0:
                choix = autre_sortie
                distance = d2
        return choix

    def deplacer(self, i: int, j: int, nb: int, direction: str, silencieux: bool = True) -> int:
        ''' effectue le déplacement dans la direction demandée d'au maximum
            nb occupants actuellement en ligne i et colonne j.
            Le déplacement est limité par la capacité d'accueil (5) de la case visée.
            Cette fonction renvoie le nombre d'occupants déplacés.
            IL N'EST PAS NECESSAIRE DE COMPRENDRE LE CODE DE CETTE METHODE.
        '''
        d = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}
        nv_i, nv_j = i + d[direction][0], j + d[direction][1]
        nb_dep = min(nb, 5 - self.grille[nv_i][nv_j], self.grille[i][j])
        if nb_dep > 0:
            if not silencieux:
                print("déplacement de ", nb_dep,
                      " occupant(s) (", i, ",", j, ") vers ", direction)
            self.grille[i][j] = self.grille[i][j] - nb_dep
            self.grille[nv_i][nv_j] = self.grille[nv_i][nv_j] + nb_dep
        return nb_dep

    def alerter(self, silencieux: bool = True) -> bool:
        ''' permet de simuler une alerte : chaque occupant se déplace d'une case
            vers la sortie qui lui est conseillée par la méthode choix_sortie.
            Cette méthode renvoie True si des déplacements ont pu avoir lieu, False sinon.
            IL N'EST PAS NECESSAIRE DE COMPRENDRE LE CODE DE CETTE METHODE.
        '''
        old_grille = deepcopy(self.grille)
        modif = False
        for i in range(len(self.grille)):
            for j in range(len(self.grille[i])):
                if old_grille[i][j] > 0:
                    sortie_i, sortie_j = self.choix_sortie(i, j)
                    dx, dy = sortie_j-j, sortie_i-i
                    if dx == 0 and dy == 0:
                        if not silencieux:
                            print("évacuation d'un occupant (", i, ",", j, ")")
                        self.grille[i][j] = self.grille[i][j] - 1
                        nb_dep = 1
                    else:
                        mvt_possibles = []
                        if dx > 0:
                            mvt_possibles.append("E")
                        elif dx < 0 and j > 0:
                            mvt_possibles.append("O")
                        if dy > 0:
                            mvt_possibles.append("S")
                        elif dy < 0 and i > 0:
                            mvt_possibles.append("N")
                        shuffle(mvt_possibles)
                        nb_dep = self.deplacer(
                            i, j, old_grille[i][j], mvt_possibles[0], silencieux)
                        if nb_dep == 0 and len(mvt_possibles) > 1:
                            nb_dep = self.deplacer(
                                i, j, old_grille[i][j], mvt_possibles[1], silencieux)
                    if nb_dep > 0:
                        modif = True
        return modif

    def __str__(self) -> str:
        ''' Cette méthode permet de convertir une pièce en chaîne de caractères.
            Ainsi, si p1 est une pièce, l'instruction print(p1) permettra d'afficher l'état actuel de la pièce dans la console.
            IL N'EST PAS NECESSAIRE DE COMPRENDRE LE CODE DE CETTE METHODE.
        '''
        s = "  "
        for j in range(self.j_max+1):
            if (0, j) in self.sorties:
                s = s + "P  "
            else:
                s = s + "   "
        s = s + "\n"
        for i in range(len(self.grille)):
            if (i, 0) in self.sorties:
                s = s + "P"
            else:
                s = s + " "
            s = s + str(self.grille[i])
            if i != 0 and i != self.i_max and (i, self.j_max) in self.sorties:
                s = s + "P\n"
            else:
                s = s + "\n"
        s = s + "  "
        for j in range(self.j_max+1):
            if (self.i_max, j) in self.sorties:
                s = s + "P  "
            else:
                s = s + "   "
        return s + "\n"


def evacuation(p: Piece, silencieux: bool = True) -> int:
    ''' simule l'évacuation de la pièce et renvoie le nombre de tours nécessaire.
        A chaque tour, chacun des occupants se déplace, si possible, d'une case
        vers la sortie la plus proche. Si le paramètre silencieux vaut false,
        l'état de la pièce à chaque tour est affiché dans la console.
        A FAIRE EN PARTIE 1
    '''
    pass


def test_nb_occupants_restants():
    ''' Jeux de tests proposés pour la méthode nb_occupants_restants de la classe Piece.
    '''
    p1 = Piece(5, 7)
    p1.ajouter_sortie("N", 5)
    reussite = True
    if p1.nb_occupants_restants() != 0:
        print("La méthode nb_restants devrait renvoyer 0 quand la pièce est vide.")
        reussite = False
    n1 = randint(1, 5)
    cases_occupees = {(0, 3): 4, (0, 1): 2, (3, 4): 3, (4, 0): n1, (4, 3): 2}
    for c in cases_occupees:
        p1.ajouter_occupants(c[0], c[1], cases_occupees[c])
    if p1.nb_occupants_restants() != 11 + n1:
        print("La méthode nb_restants renvoie",
              p1.nb_occupants_restants(), " au lieu", 11 + n1)
        reussite = False
    if reussite == True:
        print("Pas de problème détecté pour l'instant avec nb_occupants_restants. Il faudra vérifier que l'IHM affiche maintenant le bon nombre d'occupants restants.")


def test_evacuation(silencieux: bool = True):
    ''' Jeux de tests proposés pour la fonction evacuation.
    '''
    p1 = Piece(5, 7)
    p1.ajouter_sortie("N", 5)
    n1 = randint(1, 5)
    situations = [{"nom": "essai1", "cases_occupees": {(0, 3): 3, (1, 1): 1, (3, 2): 5}, "temps_attendu": 11},
                  {"nom": "essai2", "cases_occupees": {
                      (0, 3): 4, (0, 1): 2, (3, 4): 3, (4, 0): 1, (4, 3): 2}, "temps_attendu": 14},
                  {"nom": "essai3", "cases_occupees": {(0, 3): 1, (0, 1): 2, (3, 4): 1, (4, 0): 3, (4, 3): 5}, "temps_attendu": 15}]
    verif = True
    for s in situations:
        for c, nb in s["cases_occupees"].items():
            p1.ajouter_occupants(c[0], c[1], nb)
        nbT = evacuation(p1, silencieux)
        if nbT != s["temps_attendu"]:
            print("La fonction evacuation renvoie ", nbT,
                  " au lieu de ", s["temps_attendu"], " pour ", s["nom"])
            verif = False
    if verif:
        print("Pas de problème détecté pour l'instant avec l'évacuation. Il faudra vérifier avec l'IHM que les évacuations n'échouent plus.")


def test_ajouter_sortie():
    ''' Jeux de tests proposés pour tester les modifications apportées à la méthode ajouter_sortie de la classe Piece.
    '''
    p1 = Piece(5, 7)
    p1.ajouter_sortie("N", 5)
    n1 = randint(1, 5)
    p1.ajouter_sortie("S", n1)
    n2 = randint(1, 5)
    p1.ajouter_sortie("E", n2)
    p1.ajouter_sortie("O", 1)
    if p1.sorties == [(0, 5), (4, n1), (n2, 6), (1, 0)]:
        print("Pas de problème détecté avec le jeu de tests pour la méthode ajouter_sortie. Il faudra vérifier que l'ajout de sortie à l'est ou au sud de la pièce est maintenant possible via l'IHM.")
    else:
        print("L'ajout des sorties ne fonctionne pas correctement.")


def test_choix_sortie():
    ''' Jeux de tests proposés pour tester les modifications apportées à la méthode choix_sortie de la classe Piece.
    '''
    p1 = Piece(5, 7)
    # Afin de pouvoir tester choix_sortie indépendamment de ajouter_sortie,
    # on effectue ici une modification directe de l'attribut sorties de p1
    p1.sorties = [(0, 5), (4, 1), (3, 6), (1, 0)]
    try:
        assert p1.choix_sortie(0, 3) == (0, 5)
        assert p1.choix_sortie(0, 1) == (1, 0)
        assert p1.choix_sortie(1, 2) == (1, 0)
        assert p1.choix_sortie(3, 4) == (3, 6)
        assert p1.choix_sortie(4, 0) == (4, 1)
        assert p1.choix_sortie(4, 3) == (4, 1)
        print("Pas de problème détecté avec le jeu de tests pour la méthode choix_sortie. Il faudra vérifier avec l'IHM que les occupants n'utilisent plus uniquement la première sortie lors des alertes.")
    except:
        print("La méthode choix_sortie ne renvoie pas la réponse attendue sur au moins l'un des tests.")


if __name__ == "__main__":
    test_nb_occupants_restants()
    test_evacuation(False)
    test_ajouter_sortie()
    test_choix_sortie()