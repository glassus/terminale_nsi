# Épreuve pratique 💻

- Rappel des conditions de passation sur [cette page](../T6_Annales/epreuve_pratique/)

- [Pdf](https://github.com/glassus/nsi/raw/master/sujets_epreuves_pratique_2021.pdf) de l'intégralité des exercices

### Exercice 1.1
!!! example "Exercice 1.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 1.2
!!! example "Exercice 1.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 2.1
!!! example "Exercice 2.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 2.2
!!! example "Exercice 2.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 3.1
!!! example "Exercice 3.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 3.2
!!! example "Exercice 3.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 4.1
!!! example "Exercice 4.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 4.2
!!! example "Exercice 4.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 5.1
!!! example "Exercice 5.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 5.2
!!! example "Exercice 5.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 6.1
!!! example "Exercice 6.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 6.2 🗹
*à noter une erreur dans la version officielle, sur la méthode ```enfile()```* 
!!! example "Exercice 6.2"
    === "Énoncé" 
        On veut écrire une classe pour gérer une file à l’aide d’une liste chaînée. On dispose d’une
        classe ```Maillon``` permettant la création d’un maillon de la chaîne, celui-ci étant constitué
        d’une valeur et d’une référence au maillon suivant de la chaîne :

        ```python linenums='1'
        class Maillon :
            def __init__(self,v) :
                self.valeur = v
                self.suivant = None
        ```
        Compléter la classe ```File suivante``` où l’attribut ```dernier_file``` contient le maillon
        correspondant à l’élément arrivé en dernier dans la file :

        ```python linenums='1'
        class File :
            def __init__(self) :
                self.dernier_file = None

            def enfile(self,element) :
                nouveau_maillon = Maillon(...)
                nouveau_maillon.suivant = self.dernier_file
                self.dernier_file = ...

            def est_vide(self) :
                return self.dernier_file == None

            def affiche(self) :
                maillon = self.dernier_file
                while maillon != ... :
                    print(maillon.valeur)
                    maillon = ...

            def defile(self) :
                if not self.est_vide() :
                    if self.dernier_file.suivant == None :
                        resultat = self.dernier_file.valeur
                        self.dernier_file = None
                        return resultat
                    maillon = ...
                    while maillon.suivant.suivant != None :
                        maillon = maillon.suivant
                    resultat = ...
                    maillon.suivant = None
                    return resultat
                return None
        ```
        On pourra tester le fonctionnement de la classe en utilisant les commandes
        suivantes dans la console Python :
        ```python
        >>> F = File()
        >>> F.est_vide()
        True
        >>> F.enfile(2)
        >>> F.affiche()
        2
        >>> F.est_vide()
        False
        >>> F.enfile(5)
        >>> F.enfile(7)
        >>> F.affiche()
        7
        5
        2
        >>> F.defile()
        2
        >>> F.defile()
        5
        >>> F.affiche()
        7
        ```


    === "Correction" 
        {{ correction(True,
        "
        ```python linenums='1'
        class Maillon :
            def __init__(self,v) :
                self.valeur = v
                self.suivant = None

        class File :
            def __init__(self) :
                self.dernier_file = None

            def enfile(self,element) :
                nouveau_maillon = Maillon(element)
                nouveau_maillon.suivant =  self.dernier_file
                self.dernier_file = nouveau_maillon

            def est_vide(self) :
                return self.dernier_file == None

            def affiche(self) :
                maillon = self.dernier_file
                while maillon != None :
                    print(maillon.valeur)
                    maillon = maillon.suivant

            def defile(self) :
                if not self.est_vide() :
                    if self.dernier_file.suivant == None :
                        resultat = self.dernier_file.valeur
                        self.dernier_file = None
                        return resultat
                    maillon = self.dernier_file
                    while maillon.suivant.suivant != None :
                        maillon = maillon.suivant
                    resultat = maillon.suivant.valeur
                    maillon.suivant = None
                    return resultat
                return None


        ```
        "
        ) }}



### Exercice 7.1
!!! example "Exercice 7.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 7.2
!!! example "Exercice 7.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 8.1
!!! example "Exercice 8.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 8.2
!!! example "Exercice 8.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 9.1
!!! example "Exercice 9.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 9.2
!!! example "Exercice 9.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 10.1
!!! example "Exercice 10.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 10.2
!!! example "Exercice 10.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 11.1
!!! example "Exercice 11.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 11.2
!!! example "Exercice 11.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 12.1
!!! example "Exercice 12.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 12.2
!!! example "Exercice 12.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 13.1
!!! example "Exercice 13.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 13.2
!!! example "Exercice 13.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 14.1
!!! example "Exercice 14.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 14.2
!!! example "Exercice 14.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 15.1
!!! example "Exercice 15.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 15.2
!!! example "Exercice 15.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 16.1
!!! example "Exercice 16.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 16.2
!!! example "Exercice 16.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 17.1
!!! example "Exercice 17.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 17.2
!!! example "Exercice 17.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 18.1
!!! example "Exercice 18.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 18.2
!!! example "Exercice 18.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 19.1
!!! example "Exercice 19.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 19.2
!!! example "Exercice 19.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 20.1
!!! example "Exercice 20.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 20.2
!!! example "Exercice 20.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 21.1
!!! example "Exercice 21.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 21.2
!!! example "Exercice 21.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 22.1
!!! example "Exercice 22.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 22.2
!!! example "Exercice 22.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 23.1
!!! example "Exercice 23.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 23.2
!!! example "Exercice 23.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 24.1
!!! example "Exercice 24.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 24.2
!!! example "Exercice 24.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 25.1
!!! example "Exercice 25.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 25.2
!!! example "Exercice 25.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 26.1
!!! example "Exercice 26.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 26.2
!!! example "Exercice 26.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 27.1
!!! example "Exercice 27.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 27.2
!!! example "Exercice 27.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 28.1
!!! example "Exercice 28.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 28.2
!!! example "Exercice 28.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 29.1
!!! example "Exercice 29.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 29.2
!!! example "Exercice 29.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 30.1
!!! example "Exercice 30.1"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 30.2
!!! example "Exercice 30.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}




