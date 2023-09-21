# Exercices


         
{{ initexo(0) }}


!!! example "{{ exercice() }}"
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
        


!!! example "{{ exercice() }}"
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
        

!!! example "{{ exercice() }}"
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
        
  

!!! example "{{ exercice() }}"
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
    !!! example "{{ exercice() }}"
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
            



!!! example "{{ exercice() }}"
    [Exercice 32.2](../../T6_6_Epreuve_pratique/BNS_2023/#exercice-322){. target="_blank"} de la BNS 2023.



!!! example "{{ exercice() }}"
    Exercice 2 Partie A du sujet [Métropole Septembre 2022](../../T6_Annales/data/2022/2022_Metropole_Septembre.pdf){. target="_blank"}

    ??? tip "Correction Q1.a"
        La liste ```v``` contient 5 éléments.

    ??? tip "Correction Q1.b"
        ```v[1].nom()``` renvoie ```Les goélands```.

        :warning: la classe ```Villa``` possède un attribut ```nom```  ET une méthode ```nom()```. Ceci est affreux et provoquerait une erreur lors de l'appel à la méthode ```nom()```. 

    ??? tip "Correction Q1.c"
        ```python
        def surface(self):
            return self.sejour.sup + self.ch1.sup + self.ch2.sup
        ```
    
    ??? tip "Correction Q2"
        ```python
        for villa in v:
            if villa.eqCuis == "eq":
                print(villa.nom)
        ```

        ou bien

        ```python
        for villa in v:
            if villa.equip() == "eq":
                print(villa.nom)
        ```


!!! example "{{ exercice() }}"
    Exercice 5 du sujet [Métropole J1 2022](../../T6_Annales/data/2022/2022_Metropole_J1.pdf){. target="_blank"}

    ??? tip "Correction Q1"
        Instruction 3 : ```joueur1 = Joueur("Sniper", 319, "A")``` 

    ??? tip "Correction Q2.a"
        ```python linenums='1'
        def redevenir_actif(self):
            if self.est_actif == False:
                self.est_actif = True
        ```         
        ou mieux : 
        ```python linenums='1'
        def redevenir_actif(self):
            if not self.est_actif:
                self.est_actif = True
        ``` 
    
    ??? tip "Correction Q2.b"
        ```python linenums='1'
        def nb_tirs_recus(self):
            return len(self.liste_id_tirs_recus)
        ```

    ??? tip "Correction Q3.a"
        Le test est le **test 1**.

    ??? tip "Correction Q3.b"
        Si un joueur a été touché par un tir allié, son score diminue de 20 points.

    ??? tip "Correction Q4"
        ```python linenums='1'
        if participant.est_determine() == True:
            self.incremente_score(40)
        ```
        ou mieux :
        ```python linenums='1'
        if participant.est_determine():
            self.incremente_score(40)
        ```       
        
        
!!! example "{{ exercice() }}"
    Exercice 2 du sujet [La Réunion J1 2022](../../T6_Annales/data/2022/2022_LeReunion_J1.pdf){. target="_blank"}

    ??? tip "Correction Q1.a"
        ```python linenums='1'
        i = 0
        while i < len(Mousse) and Mousse[i] != None:
            i += 1
        return i
        ```       

    ??? tip "Correction Q1.b"
        ```python linenums='1'
        def placeBulle(B):
            i = donnePremierIndiceLibre(Mousse)
            if i != 6:
                Mousse[i] = B 
        ```
    
    ??? tip "Correction Q2"
        ```python linenums='1'
        def bullesEnContact(B1,B2):
            return distanceEntreBulles(B1, B2) <= B1.rayon + B2.rayon
        ```
        
    ??? tip "Correction Q3"
        ```python linenums='1' hl_lines='10 14 15 18'
        def collision(indPetite, indGrosse, Mousse) :
            """
            Absorption de la plus petite bulle d’indice indPetite
            par la plus grosse bulle d’indice indGrosse. Aucun test
            n’est réalisé sur les positions.
            """
            # calcul du nouveau rayon de la grosse bulle
            surfPetite = pi * Mousse[indPetite].rayon**2
            surfGrosse = pi * Mousse[indGrosse].rayon**2
            surfGrosseApresCollision = surfPetite + surfGrosse = pi
            rayonGrosseApresCollision = sqrt(surfGrosseApresCollision/pi)
            
            #réduction de 50% de la vitesse de la grosse bulle
            Mousse[indGrosse].dirx = 0.5 * Mousse[indGrosse].dirx
            Mousse[indGrosse].diry = 0.5 * Mousse [indGrosse].diry
            
            #suppression de la petite bulle dans Mousse
            Mousse[indPetite] = None
        ```

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