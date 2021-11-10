# Épreuve pratique 💻

- Rappel des conditions de passation sur [cette page](../T6_Annales/epreuve_pratique/)

- [Pdf](https://github.com/glassus/nsi/raw/master/sujets_epreuves_pratique_2021.pdf) de l'intégralité des exercices

<!-- □  🗹 -->

### Exercice 01.1 □
!!! example "Exercice 01.1"
    === "Énoncé" 
        Programmer la fonction `recherche`, prenant en paramètre un tableau non vide `tab` (type `list`) d'entiers et un entier `n`, et qui renvoie l'indice de la **dernière** occurrence de l'élément cherché. Si l'élément n'est pas présent, la fonction renvoie la longueur du tableau.

        Exemples
        ```python
        >>> recherche([5, 3],1)
        2
        >>> recherche([2,4],2)
        0
        >>> recherche([2,3,5,2,4],2)
        3
        ```

    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 01.2
!!! example "Exercice 01.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 02.1 □
!!! example "Exercice 02.1"
    === "Énoncé" 
        Programmer la fonction ```moyenne```   prenant en paramètre un tableau d'entiers ```tab```   (type
        `list`) qui renvoie la moyenne de ses éléments si le tableau est non vide et affiche
        'erreur' si le tableau est vide.

        Exemples :
        ```python
        >>> moyenne([5,3,8])
        5.333333333333333
        >>> moyenne([1,2,3,4,5,6,7,8,9,10])
        5.5
        >>> moyenne([])
        'erreur'
        ```
    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 02.2
!!! example "Exercice 02.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 03.1 □
!!! example "Exercice 03.1"
    === "Énoncé" 
        Programmer la fonction `multiplication`, prenant en paramètres deux nombres entiers
        `n1` et `n2`, et qui renvoie le produit de ces deux nombres.
        Les seules opérations autorisées sont l’addition et la soustraction. 

    === "Correction" 
        {{ correction(False,
        "
        ```python linenums='1'
        def multiplication(n1, n2):
            acc = 0
            for _ in range(n2):
                acc += n1
            return acc

        ```

        "
        ) }}



### Exercice 03.2 
!!! example "Exercice 03.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 04.1 □
!!! example "Exercice 04.1"
    === "Énoncé" 
        Écrire une fonction qui prend en paramètre un tableau d'entiers non vide et qui renvoie la
        moyenne de ces entiers. La fonction est spécifiée ci-après et doit passer les assertions
        fournies.
        ```python
        def moyenne (tab):
            '''
            moyenne(list) -> float
            Entrée : un tableau non vide d'entiers
            Sortie : nombre de type float
            Correspondant à la moyenne des valeurs présentes dans le
            tableau
            '''

        assert moyenne([1]) == 1
        assert moyenne([1,2,3,4,5,6,7] == 4
        assert moyenne([1,2]) == 1.5
        ```
    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 04.2
!!! example "Exercice 04.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 05.1 □
!!! example "Exercice 05.1"
    === "Énoncé" 
        On modélise la représentation binaire d'un entier non signé par un tableau d'entiers dont
        les éléments sont 0 ou 1. Par exemple, le tableau `[1, 0, 1, 0, 0, 1, 1]` représente
        l'écriture binaire de l'entier dont l'écriture décimale est
        `2**6 + 2**4 + 2**1 + 2**0 = 83`.
        À l'aide d'un parcours séquentiel, écrire la fonction convertir répondant aux
        spécifications suivantes :

        ```python
        def convertir(T):
            """
            T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
            représentant un entier écrit en binaire. Renvoie l'écriture
            décimale de l'entier positif dont la représentation binaire
            est donnée par le tableau T
            """
        ```
        Exemple :
        ```python
        >>> convertir([1, 0, 1, 0, 0, 1, 1])
        83
        >>> convertir([1, 0, 0, 0, 0, 0, 1, 0])
        130
        ```

    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 05.2
!!! example "Exercice 05.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 06.1 □
!!! example "Exercice 06.1"
    === "Énoncé" 
        On s’intéresse au problème du rendu de monnaie. On suppose qu’on dispose d’un
        nombre infini de billets de 5 euros, de pièces de 2 euros et de pièces de 1 euro.
        Le but est d’écrire une fonction nommée `rendu` dont le paramètre est un entier positif non
        nul `somme_a_rendre` et qui retourne une liste de trois entiers `n1`, `n2` et `n3` qui
        correspondent aux nombres de billets de 5 euros (`n1`) de pièces de 2 euros (`n2`) et de
        pièces de 1 euro (`n3`) à rendre afin que le total rendu soit égal à `somme_a_rendre`.

        On utilisera un algorithme glouton : on commencera par rendre le nombre maximal de
        billets de 5 euros, puis celui des pièces de 2 euros et enfin celui des pièces de 1 euros.

        Exemples :
        ```python
        >>> rendu(13)
        [2,1,1]
        >>> rendu(64)
        [12,2,0]
        >>> rendu(89)
        [17,2,0]
        ```

    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 06.2 □
*à noter une erreur dans la version officielle, sur la méthode ```enfile()```* 
!!! example "Exercice 06.2"
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



### Exercice 07.1 □
!!! example "Exercice 07.1"
    === "Énoncé" 
        On s’intéresse à la suite d’entiers définie par
        `U1 = 1`, `U2 = 1` et, pour tout entier naturel `n`, par `Un+2 = Un+1 + Un`.

        Elle s’appelle la suite de Fibonnaci.

        Écrire la fonction `fibonacci` qui prend un entier `n > 0` et qui renvoie l’élément d’indice
        `n` de cette suite.

        On utilisera une programmation dynamique (pas de récursivité).

        Exemple :

        ```python
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(25)
        75025
        >>> fibonacci(45)
        1134903170
        ```

    === "Correction" 
        {{ correction(False,
        "
        ```python linenums='1'
        def fibonnaci(n):
            d = {}
            d[1] = 1
            d[2] = 1
            for k in range(3, n+1):
                d[k] = d[k-1] + d[k-2]
            return d[n]
        ```

        "
        ) }}



### Exercice 07.2
!!! example "Exercice 07.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 08.1 □
!!! example "Exercice 08.1"
    === "Énoncé" 
        Écrire une fonction `recherche` qui prend en paramètres `caractere`, un caractère, et
        `mot`, une chaîne de caractères, et qui renvoie le nombre d’occurrences de `caractere`
        dans `mot`, c’est-à-dire le nombre de fois où `caractere` apparaît dans `mot`.

        Exemples :
        ```python
        >>> recherche('e', "sciences")
        2
        >>> recherche('i',"mississippi")
        4
        >>> recherche('a',"mississippi")
        0
        ```
    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 08.2
!!! example "Exercice 08.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 09.1 □
!!! example "Exercice 09.1"
    === "Énoncé" 
        Soit le couple (`note`,`coefficient`):

        - `note` est un nombre de type flottant (`float`) compris entre 0 et 20 ;
        - `coefficient` est un nombre entier positif.
        
        Les résultats aux évaluations d'un élève sont regroupés dans une liste composée de
        couples (`note`,`coefficient`).

        Écrire une fonction moyenne qui renvoie la moyenne pondérée de cette liste donnée en
        paramètre.

        Par exemple, l’expression `moyenne([(15,2),(9,1),(12,3)])` devra renvoyer le
        résultat du calcul suivant :

        $\dfrac{2 \times 15 + 1 \times 9 + 3 \times 12 }{2+1+3}=11,83$

    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 09.2
!!! example "Exercice 09.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 10.1 □
!!! example "Exercice 10.1"
    === "Énoncé" 
        Écrire une fonction `maxi` qui prend en paramètre une liste `tab` de nombres entiers et renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la première apparition de ce maximum dans la liste.

        Exemple :
        ```python
        >>> maxi([1,5,6,9,1,2,3,7,9,8])
        (9,3)
        ```

    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 10.2 □
!!! example "Exercice 10.2"
    === "Énoncé" 
        Cet exercice utilise des piles qui seront représentées en Python par des listes (type `list`).

        On rappelle que l’expression `T1 = list(T)` fait une copie de `T `indépendante de `T`, que
        l’expression `x = T.pop()` enlève le sommet de la pile `T` et le place dans la variable `x` et,
        enfin, que l’expression `T.append(v)` place la valeur `v` au sommet de la pile `T`.

        Compléter le code Python de la fonction positif ci-dessous qui prend une pile `T` de
        nombres entiers en paramètre et qui renvoie la pile des entiers positifs dans le même
        ordre, sans modifier la variable `T`.

        ```python linenums='1'
        def positif(T):
            T2 = ...(T)
            T3 = ...
            while T2 != []:
                x = ...
                if ... >= 0:
                    T3.append(...)
            T2 = []
            while T3 != ...:
                x = T3.pop()
                ...
            print('T = ',T)
            return T2
        ```

        Exemple :
        ```python
        >>> positif([-1,0,5,-3,4,-6,10,9,-8 ])
        T = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
        [0, 5, 4, 10, 9]
        ```
    === "Correction" 
        {{ correction(True,
        "
        ```python linenums='1'
        def positif(T):
            T2 = list(T)
            T3 = []
            while T2 != []:
                x = T2.pop()
                if x >= 0:
                    T3.append(x)
            T2 = [] # <- NB : cette ligne est inutile
            while T3 != []:
                x = T3.pop()
                T2.append(x)
            print('T = ',T)
            return T2
        ```        
        "
        ) }}



### Exercice 11.1 □
!!! example "Exercice 11.1"
    === "Énoncé" 
        Écrire une fonction `conv_bin` qui prend en paramètre un entier positif `n` et renvoie un
        couple (`b,bit)` où :

        - `b` est une liste d'entiers correspondant à la représentation binaire de `n`;
        - `bit` correspond aux nombre de bits qui constituent `b`.

        Exemple :
        ```python
        >>> conv_bin(9)
        ([1,0,1,1],4)
        ```

        Aide :

        - l'opérateur `//` donne le quotient de la division euclidienne : `5//2` donne `2` ;
        - l'opérateur `%` donne le reste de la division euclidienne :` 5%2` donne `1` ;
        - `append` est une méthode qui ajoute un élément à une liste existante :
        Soit `T=[5,2,4]`, alors `T.append(10)` ajoute `10` à la liste `T`. Ainsi, `T` devient
        `[5,2,4,10]`.
        - `reverse` est une méthode qui renverse les éléments d'une liste.
        Soit `T=[5,2,4,10]`. Après `T.reverse()`, la liste devient `[10,4,2,5]`.

        On remarquera qu’on récupère la représentation binaire d’un entier `n` en partant de la gauche en appliquant successivement les instructions :

        `b = n%2`
        
        `n = n//2`

        répétées autant que nécessaire.

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




