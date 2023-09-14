# Exercices


         



!!! example "Exercice 1"
    === "Énoncé"
        1. Écrire une classe ```Eleve``` qui contiendra les attributs ```nom```, ```classe``` et ```note```.
        2. Instancier trois élèves de cette classe.
        3. Écrire une fonction ```compare(eleve1, eleve2)``` qui renvoie le nom de l'élève ayant la meilleure note (on ne traitera pas à part le cas d'égalité).

        !!! info "Exemple d'utilisation de la classe"
            ```python
            >>> riri = Eleve("Henri", "TG2", 12)
            >>> fifi = Eleve("Philippe", "TG6", 15)
            >>> loulou = Eleve("Louis", "TG1", 8)
            >>> compare(riri, fifi)
            'Philippe'
            ```

    === "Correction"

        
        ```python linenums='1'
        class Eleve:
            def __init__(self, nom, classe, note):
                self.nom = nom
                self.classe = classe
                self.note = note
                
        def compare(eleve1, eleve2):
            if eleve1.note > eleve2.note:
                return eleve1.nom
            else:
                return eleve2.nom
        ```
        


!!! example "Exercice 2"
    === "Énoncé"
        Écrire une classe ```TriangleRect``` qui contiendra les attributs ```cote1```, ```cote2``` et ```hypotenuse```.

        La méthode constructeur ne prendra en paramètres que ```cote1``` et ```cote2```, l'attribut ```hypotenuse``` se calculera automatiquement.

        !!! info "Exemple d'utilisation de la classe"

            ```python
            >>> mon_triangle = TriangleRect(3,4)
            >>> mon_triangle.cote1
            3
            >>> mon_triangle.cote2
            4
            >>> mon_triangle.hypotenuse
            5.0
            ```



    === "Correction"
        
        ```python linenums='1'
        class TriangleRect:
            def __init__(self, c1, c2):
                self.cote1 = c1
                self.cote2 = c2
                self.hypotenuse = (self.cote1**2 + self.cote2**2)**0.5
        ```
        

!!! example "Exercice 3"
    === "Énoncé"
        1. Écrire une classe ```Chrono``` qui contiendra les attributs ```heures```, ```minutes``` et ```secondes```.
        2. Doter la classe d'une méthode ```affiche()``` qui fera affichera le temps ```t```.
        3. Doter la classe d'une méthode ```avance(s)``` qui fera avancer le temps ```t``` de ```s``` secondes.

        !!! info "Exemple d'utilisation de la classe"

            ```python
            >>> t = Chrono(17,25,38)
            >>> t.heures
            17
            >>> t.minutes
            25
            >>> t.secondes
            38
            >>> t.affiche()
            'Il est 17 heures, 25 minutes et 38 secondes'
            >>> t.avance(27)
            >>> t.affiche()
            'Il est 17 heures, 26 minutes et 5 secondes'
            ```

        ??? tip "Aide"
            On pourra utiliser les opérateurs :
            
            - ```%```, qui calcule le reste d'une division euclidienne.
            - ```//```, qui calcule le quotient d'une division euclidienne.

    === "Correction"
        
        ```python linenums='1'
        class Chrono:
            def __init__(self, h, m, s):
                self.heures = h
                self.minutes = m
                self.secondes = s
                
            def affiche(self):
                print("Il est {} heures, {} minutes \
                et {} secondes".format(self.heures, self.minutes, self.secondes))

            def avance(self, s):
                self.secondes += s

                # il faut ajouter les minutes supplémentaires si les secondes
                # dépassent 60
                self.minutes += self.secondes // 60

                # il ne faut garder des secondes que ce qui n'a pas servi
                # à fabriquer des minutes supplémentaires
                self.secondes = self.secondes % 60

                # il faut ajouter les heures supplémentaires si les minutes
                # dépassent 60
                self.heures += self.minutes // 60

                # il ne faut garder des minutes que ce qui n'a pas servi
                # à fabriquer des heures supplémentaires
                self.minutes = self.minutes % 60
        ```
        
  

!!! example "Exercice 4"
    === "Énoncé"
        Écrire une classe ```Player``` qui :

        - ne prendra aucun argument lors de son instanciation.
        - affectera à chaque objet créé un attribut ```energie``` valant 3 par défaut. 
        - affectera à chaque objet créé un attribut ```alive``` valant ```True``` par défaut.
        - fournira à chaque objet une méthode ```blessure()``` qui diminue l'attribut ```energie``` de 1.
        - fournira à chaque objet une méthode ```soin()``` qui augmente l'attribut ```energie``` de 1.
        - si l'attribut ```energie``` passe à 0, l'attribut ```alive``` doit passer à ```False``` et ne doit plus pouvoir évoluer.

        !!! info "Exemple d'utilisation de la classe"

            ```python
            >>> mario = Player()
            >>> mario.energie
            3
            >>> mario.soin()
            >>> mario.energie
            4
            >>> mario.blessure()
            >>> mario.blessure()
            >>> mario.blessure()
            >>> mario.alive
            True
            >>> mario.blessure()
            >>> mario.alive
            False
            >>> mario.soin()
            >>> mario.alive
            False
            >>> mario.energie
            0
            ```

    === "Correction"
        
        ```python linenums='1'
        class Player:
            def __init__(self):
                self.energie = 3
                self.alive = True
            
            def blessure(self):
                self.energie -= 1
                if self.energie == 0:
                    self.alive = False
                
            def soin(self):
                if self.energie > 0:
                    self.energie += 1
        ```
        

!!! capytale "À faire sur Capytale : [activité 2ef0-54279](https://capytale2.ac-paris.fr/web/c/2ef0-54279/mlc){. target="_blank"}"
    !!! example "Exercice 5"
        === "Énoncé"
            Créer une classe ```CompteBancaire``` dont la méthode constructeur recevra en paramètres :

            - un attribut ```titulaire``` stockant le nom du propriétaire.
            - un attribut ```solde``` contenant le solde disponible sur le compte.  
            
            Cette classe contiendra deux méthodes ```retrait()``` et ```depot()``` qui permettront de retirer ou de déposer de l'argent sur le compte. 
        
            !!! info "Exemple d'utilisation de la classe"
                ```python
                >>> compteGL = CompteBancaire("G.Lassus", 1000)
                >>> compteGL.retrait(50)
                Vous avez retiré 50 euros
                Solde actuel du compte : 950 euros
                >>> compteGL.retrait(40000)
                Retrait impossible
                >>> compteGL.depot(10000000)
                Vous avez déposé 10000000 euros
                Solde actuel du compte : 10000950 euros
                ```
                
        === "Correction"
            {#
            ```python linenums='1'
            class CompteBancaire:
                def __init__(self, titulaire, solde):
                    self.titulaire = titulaire
                    self.solde = solde
                    
                def retrait(self, somme):
                    if somme > self.solde:
                        print("Retrait impossible")
                    else :
                        self.solde -= somme
                        print("Vous avez retiré {} euros".format(somme))
                        print("Solde actuel du compte : {} euros".format(self.solde))

                def depot(self, somme):
                    self.solde += somme
                    print("Vous avez déposé {} euros".format(somme))
                    print("Solde actuel du compte : {} euros".format(self.solde))
            ```
            #}



!!! abstract "Exercice 6"
    === "Énoncé"
        **Cet exercice est l'exercice 5.2 de la BNS (version 2022)**.

        On dispose d’un programme permettant de créer un objet de type `PaquetDeCarte`,
        selon les éléments indiqués dans le code ci-dessous.
        Compléter ce code aux endroits indiqués par `#A compléter`, puis ajouter des
        assertions dans l’initialiseur de `Carte`, ainsi que dans la méthode `getCarteAt()`.

        ```python linenums='1'
        class Carte:
            """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
            def __init__(self, c, v):
                self.Couleur = c
                self.Valeur = v

            """Renvoie le nom de la Carte As, 2, ... 10, 
               Valet, Dame, Roi"""
            def getNom(self):
                if ( self.Valeur > 1 and self.Valeur < 11):
                    return str( self.Valeur)
                elif self.Valeur == 11:
                    return "Valet"
                elif self.Valeur == 12:
                    return "Dame"
                elif self.Valeur == 13:
                    return "Roi"
                else:
                    return "As"

            """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
            def getCouleur(self):
                return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

        class PaquetDeCarte:
            def __init__(self):
                self.contenu = []

            """Remplit le paquet de cartes"""
            def remplir(self):
                ??? = [ ??? for couleur in range(1, ???) for valeur in range( 1, ???)]

            """Renvoie la Carte qui se trouve a  la position donnee"""
            def getCarteAt(self, pos):
                if 0 <= pos < ??? :
                    return ???
        ```

        Exemple :

        ```python
        >>> unPaquet = PaquetDeCarte()
        >>> unPaquet.remplir()
        >>> uneCarte = unPaquet.getCarteAt(20)
        >>> print(uneCarte.getNom() + " de " + uneCarte.getCouleur())
        8 de coeur
        ```

    === "Correction"
        {#
        ```python linenums='1'
        class Carte:
            """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
            def __init__(self, c, v):
                assert c in range(1,5)
                assert v in range(1,14)
                self.Couleur = c
                self.Valeur = v

            """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
            def getNom(self):
                if (self.Valeur > 1 and self.Valeur < 11):
                    return str( self.Valeur)
                elif self.Valeur == 11:
                    return "Valet"
                elif self.Valeur == 12:
                    return "Dame"
                elif self.Valeur == 13:
                    return "Roi"
                else:
                    return "As"

            """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
            def getCouleur(self):
                return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur - 1]

        class PaquetDeCarte:
            def __init__(self):
                self.contenu = []

            """Remplit le paquet de cartes"""
            def remplir(self):
                self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(1, 14)]

            """Renvoie la Carte qui se trouve à la position donnée"""
            def getCarteAt(self, pos):
                if 0 <= pos < len(self.contenu) :
                    return self.contenu[pos]

        ```
        #}

{#
!!! abstract "DS02"
    === "Sujet"
        ## Gestion d'une bibliothèque

        Il s'agit de gérer les livres d'une bibliothèque, à l'aide de deux classes, la classe `Livre` et la classe `Bibliotheque`.

        Le cahier des charges ci-dessous comporte la description des deux classes, ainsi qu'un exemple concret de leur utilisation.

        ### ▸ classe `Livre` 
        Elle comporte 3 attributs :

        - `titre` : le titre du livre
        - `auteur` : le nom de l'auteur
        - `etat` : un nombre entier entre 0 et 5. Si l'état vaut 0, le livre est trop abîmé et doit être retiré de la bibliothèque. L'état d'un livre ne peut pas être négatif.

        Elle comporte 2 méthodes :

        - `degrade` : enlève 1 à l'état du livre.
        - `description` : affiche les renseignements sur le livre


        ### ▸ classe `Bibliotheque`

        Elle comporte 1 attribut :

        - `livres` : une liste (vide à la création de l'objet)

        Elle comporte 3 méthodes :

        - `ajoute` : prend un livre en paramètre et l'ajoute à la bibliothèque.
        - `supprime_livres_abimes` : enlève de la bibliothèque les livres trop abîmés.
        - `inventaire` : affiche le contenu de la bibliothèque


        ### ▸ Exemple d'utilisation des classes 

        ```python
        >>> ma_bibli = Bibliotheque()
        >>> livre1 = Livre("Les Misérables", "Victor Hugo", 3)
        >>> livre2 = Livre("Les fleurs du mal", "Charles Baudelaire", 1)
        >>> ma_bibli.ajoute(livre1)
        >>> ma_bibli.ajoute(livre2)
        >>> livre1.description()
        Titre : Les Misérables
        Auteur : Victor Hugo
        Etat : 3
        >>> livre2.degrade()
        >>> livre2.description()
        Titre : Les fleurs du mal
        Auteur : Charles Baudelaire
        Etat : 0
        >>> ma_bibli.inventaire()
        -------------------------------
        contenu de ma bibliothèque :
        -------------------------------

        Titre : Les Misérables
        Auteur : Victor Hugo
        Etat : 3

        Titre : Les fleurs du mal
        Auteur : Charles Baudelaire
        Etat : 0

        >>> ma_bibli.supprime_livres_abimes()
        >>> ma_bibli.inventaire()
        -------------------------------
        contenu de ma bibliothèque :
        -------------------------------

        Titre : Les Misérables
        Auteur : Victor Hugo
        Etat : 3

        ```

        ### ▸ Question

        Proposer un code pour la classe `Livre` et la classe `Bibliotheque` répondant au cahier des charges.

    === "Correction"

        ```python linenums='1'
        class Livre():
            def __init__(self, titre, auteur, etat):
                self.titre = titre
                self.auteur = auteur
                self.etat = etat

            def degrade(self):
                if self.etat > 0:
                    self.etat -= 1

            def description(self):
                print("Titre :", self.titre)
                print("Auteur :",self.auteur)
                print("Etat :", self.etat)

        class Bibliotheque:
            def __init__(self):
                self.livres = []

            def ajoute(self, livre):
                self.livres.append(livre)

            def supprime_livres_abimes(self):
                for livre in self.livres:
                    if livre.etat == 0:
                        self.livres.remove(livre)

            def inventaire(self):
                print("---------------")
                print("contenu de ma bibliothèque :")
                print("---------------")
                for livre in self.livres:
                    livre.description()
                    print()

        ma_bibli = Bibliotheque()
        livre1 = Livre("Les Misérables", "Victor Hugo", 3)
        livre2 = Livre("Les fleurs du mal", "Charles Baudelaire", 1)
        livre1.description()
        ma_bibli.ajoute(livre1)
        ma_bibli.ajoute(livre2)
        ma_bibli.inventaire()



        ```
#}