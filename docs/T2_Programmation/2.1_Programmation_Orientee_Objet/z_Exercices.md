# Exercices


         



!!! example "Exercice 1"
    === "Énoncé"
        1. Écrire une classe ```Eleve``` qui contiendra les attributs ```nom```, ```classe``` et ```note```.
        2. Instancier trois élèves de cette classe.
        3. Écrire une fonction ```compare(eleve1, eleve2)``` qui renvoie le nom de l'élève ayant la meilleure note.

        ??? info "Exemple d'utilisation de la classe"
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

        ??? info "Exemple d'utilisation de la classe"

            ```python
            >>> mon_triangle = TriangleRect(3,4)
            >>> mon_triangle.cote1
            3
            >>> mon_triangle.cote2
            4
            >>> mon_triangle.hypotenuse
            5.0
            ```



<!--     === "Correction"

        ```python linenums='1'
        class TriangleRect:
            def __init__(self, a, b):
                self.cote1 = a
                self.cote2 = b
                self.hypotenuse = (self.cote1**2 + self.cote2**2)**0.5
        ```  -->

!!! example "Exercice 3"
    === "Énoncé"
        1. Écrire une classe ```Chrono``` qui contiendra les attributs ```heures```, ```minutes``` et ```secondes```.
        2. Doter la classe d'une méthode ```affiche()``` qui fera affichera le temps ```t```.
        3. Doter la classe d'une méthode ```avance(s)``` qui fera avancer le temps ```t``` de ```s``` secondes.

        ??? info "Exemple d'utilisation de la classe"

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
<!--     === "Correction"
        ```python linenums='1'
        class Chrono:
            def __init__(self, h, m, s):
                self.heures = h
                self.minutes = m
                self.secondes = s
                
            def affiche(self):
                return "Il est {} heures, {} minutes \
        et {} secondes".format(self.heures, self.minutes, self.secondes)

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
        ``` -->
  

!!! example "Exercice 4"
    === "Énoncé"
        Écrire une classe ```Player``` qui :

        - ne prendra aucun argument lors de son instanciation.
        - affectera à chaque objet créé un attribut ```energie``` valant 3 par défaut. 
        - affectera à chaque objet créé un attribut ```alive``` valant ```True``` par défaut.
        - fournira à chaque objet une méthode ```blessure()``` qui diminue l'attribut ```energie``` de 1.
        - fournira à chaque objet une méthode ```soin()``` qui augmente l'attribut ```energie``` de 1.
        - si l'attribut ```energie``` passe à 0, l'attribut ```alive``` doit passer à ```False``` et ne doit plus pouvoir évoluer.

        ??? info "Exemple d'utilisation de la classe"

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
                if self.energie <= 0:
                    self.alive = False
                
            def soin(self):
                if self.energie > 0:
                    self.energie += 1
        ```

!!! capytale "À faire sur Capytale : [activité 2ef0-54279](https://capytale2.ac-paris.fr/web/c-auth/list?returnto=/web/code/2ef0-54279)"
    !!! example "Exercice"
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
                
<!--         === "Correction"
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
            ``` -->

