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



    === "Correction"

        ```python linenums='1'
        class TriangleRect:
            def __init__(self, a, b):
                self.cote1 = a
                self.cote2 = b
                self.hypotenuse = (self.cote1**2 + self.cote2**2)**0.5
        ``` 

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
    === "Correction"
        ```python linenums='1'
        class Chrono:
            def __init__(self, h, m, s):
                self.heures = h
                self.minutes = m
                self.secondes = s
                
            def affiche(self):
                return "Il est {} heures, {} minutes \
        et {} secondes".format(self.heures, self.minutes, self.secondes)
        ```
        ??? info "fin de l'exercice"
            ```python linenums='1'
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
        - fournira à chaque objet une méthode ```bonus()``` qui augmente l'attribut ```energie``` de 1.
        - si l'attribut ```energie``` passe à 0, l'attribut ```alive``` doit passer à ```False``` et ne doit plus pouvoir évoluer.

        ??? info "Exemple d'utilisation de la classe"

            ```python
            >>> Mario = Player()
            >>> Mario.energie
            3
            >>> Mario.bonus()
            >>> Mario.energie
            4
            >>> Mario.blessure()
            >>> Mario.blessure()
            >>> Mario.blessure()
            >>> Mario.alive
            True
            >>> Mario.blessure()
            >>> Mario.alive
            False
            >>> Mario.bonus()
            >>> Mario.alive
            False
            >>> Mario.energie
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
                
            def bonus(self):
                if self.energie > 0:
                    self.energie += 1
        ```