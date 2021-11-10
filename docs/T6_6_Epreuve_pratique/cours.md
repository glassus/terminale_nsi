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
        ```python linenums='1'
        def recherche(tab, n):
            indice_solution = len(tab)
            for i in range(len(tab)):
                if tab[i] == n:
                    indice_solution = i
            return indice_solution
        ```
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
        L'énoncé n'est pas très clair quand il dit «d'afficher 'erreur'» (ce qui suppose un `print` et non un `return`). Nous choississons donc dans ce cas de renvoyer ```None```.

        ```python linenums='1'
        def moyenne(tab):
            if tab == []:
                print('erreur')
                return None
            else:
                somme = 0
                for elt in tab:
                    somme += elt
                return somme / len(tab)

        ```
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
        {{ correction(True,
        "
        Énoncé peu clair, on ne sait pas si ```n1``` et ```n2``` sont entiers naturels ou relatifs. Nous décidons qu'ils sont naturels.
        ```python linenums='1'
        def multiplication(n1, n2):
            resultat = 0
            for _ in range(n2):
                resultat += n1
            return resultat
        ```

        On peut proposer une solution récursive :
        ```python linenums='1'
        def multiplication_rec(n1, n2):
            if n2 == 0:
                return 0
            else:
                return n1 + multiplication_rec(n1, n2-1)
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
        ```python linenums='1'
        def moyenne(tab):
            '''
            moyenne(list) -> float
            Entrée : un tableau non vide d'entiers
            Sortie : nombre de type float
            Correspondant à la moyenne des valeurs présentes dans le
            tableau
            '''
            somme = 0
            for elt in tab:
                somme += elt
            return somme / len(tab)
        ```
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
        ```python linenums='1'
        def convertir(T):
            puissance = 0
            total = 0
            for i in range(len(T)-1, -1, -1):
                total += T[i]*(2**puissance)
                puissance += 1
            return total

        ```
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
        ```python linenums='1'
        def rendu(somme_a_rendre):
            pieces = [5, 2, 1]
            retour = [0, 0, 0]
            reste_a_rendre = somme_a_rendre
            for i in range(3):
                retour[i] = reste_a_rendre // pieces[i]
                reste_a_rendre = reste_a_rendre % pieces[i]
            return retour
        ```
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
        {{ correction(True,
        "
        On utilise un dictionnaire pour stocker au fur et à mesure les valeurs.
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
        ```python linenums='1'
        def recherche(caractere, mot):
            somme = 0
            for lettre in mot:
                if lettre == caractere:
                    somme += 1
            return somme
        ```
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

        $\dfrac{2 \times 15 + 1 \times 9 + 3 \times 12 }{2+1+3}=12,5$

    === "Correction" 
        {{ correction(True,
        "
        ```python linenums='1'
        def moyenne(tab):
            somme_notes = 0
            somme_coeffs = 0
            for devoir in tab:
                note = devoir[0]
                coeff = devoir[1]
                somme_notes += note * coeff
                somme_coeffs += coeff
            return somme_notes / somme_coeffs
        ```
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



### Exercice 10.2 🗹
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



### Exercice 12.1 □
*Ce sujet est le même que le 10.1...*  ¯\\\_(ツ)\_/¯
!!! example "Exercice 12.1"
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



### Exercice 12.2
!!! example "Exercice 12.2"
    === "Énoncé" 


    === "Correction" 
        {{ correction(True,
        "
        
        "
        ) }}



### Exercice 13.1 □
!!! example "Exercice 13.1"
    === "Énoncé" 
        Écrire une fonction `tri_selection` qui prend en paramètre une liste `tab` de nombres
        entiers et qui renvoie le tableau trié par ordre croissant.

        On utilisera l’algorithme suivant :

        - on recherche le plus petit élément du tableau, et on l'échange avec l'élément d'indice 0 ;
        - on recherche le second plus petit élément du tableau, et on l'échange avec l'élément
        d'indice 1 ;
        - on continue de cette façon jusqu'à ce que le tableau soit entièrement trié.

        Exemple :
        ```python
        >>> tri_selection([1,52,6,-9,12])
        [-9, 1, 6, 12, 52]
        ``` 

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



### Exercice 14.1 □
!!! example "Exercice 14.1"
    === "Énoncé" 
        Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre et `tab` un
        tableau de nombres, et qui renvoie le tableau des indices de `elt` dans `tab` si `elt` est dans `tab` et le tableau vide `[]` sinon.

        Exemples :
        ```python
        >>> recherche(3, [3, 2, 1, 3, 2, 1])
        [0, 3]
        >>> recherche(4, [1, 2, 3])
        []
        ```

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



### Exercice 15.1 □
!!! example "Exercice 15.1"
    === "Énoncé" 
        Écrire une fonction `RechercheMinMax` qui prend en paramètre un tableau de nombres
        non triés `tab`, et qui renvoie la plus petite et la plus grande valeur du tableau sous la
        forme d’un dictionnaire à deux clés ‘min’ et ‘max’. Les tableaux seront représentés sous
        forme de liste Python.

        Exemples :
        ```python
        >>> tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
        >>> resultat = rechercheMinMax(tableau)
        >>> resultat
        {'min': -2, 'max': 9}
        >>> tableau = []
        >>> resultat = rechercheMinMax(tableau)
        >>> resultat
        {'min': None, 'max': None}
        ```

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



### Exercice 16.1 □
!!! example "Exercice 16.1"
    === "Énoncé" 
        Écrire une fonction `moyenne` qui prend en paramètre un tableau non vide de nombres
        flottants et qui renvoie la moyenne des valeurs du tableau. Les tableaux seront
        représentés sous forme de liste Python.

        Exemples :
        ```python
        >>> moyenne([1.0])
        1.0
        >>> moyenne([1.0, 2.0, 4.0])
        2.3333333333333335
        ```

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



### Exercice 17.1 □
!!! example "Exercice 17.1"
    === "Énoncé" 
        Écrire une fonction `RechercheMin` qui prend en paramètre un tableau de nombres non
        trié `tab`, et qui renvoie l'indice de la première occurrence du minimum de ce tableau. Les
        tableaux seront représentés sous forme de liste Python.

        Exemples :
        ```python
        >>> indice_du_min([5])
        0
        >>> indice_du_min([2, 4, 1])
        2
        >>> indice_du_min([5, 3, 2, 2, 4])
        2
        ```

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



### Exercice 18.1 □
!!! example "Exercice 18.1"
    === "Énoncé" 
        Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
        un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt`
        dans `tab` si `elt` est dans `tab` et `-1` sinon.

        Exemples :
        ```python
        >>> recherche(1, [2, 3, 4])
        -1
        >>> recherche(1, [10, 12, 1, 56])
        2
        >>> recherche(50, [1, 50, 1])
        1
        >>> recherche(15, [8, 9, 10, 15])
        3
        ```

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



### Exercice 19.1 □
!!! example "Exercice 19.1"
    === "Énoncé" 
        Écrire une fonction `recherche` qui prend en paramètres un tableau `tab` de nombres
        entiers triés par ordre croissant et un nombre entier `n`, et qui effectue une recherche
        dichotomique du nombre entier `n` dans le tableau non vide `tab`.
        Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le
        tableau, `-1` sinon.

        Exemples :
        ```python
        >>> recherche([2, 3, 4, 5, 6], 5)
        3
        >>> recherche([2, 3, 4, 6, 7], 5)
        -1
        ```

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



### Exercice 20.1 □
!!! example "Exercice 20.1"
    === "Énoncé" 
        On a relevé les valeurs moyennes annuelles des températures à Paris pour la période
        allant de 2013 à 2019. Les résultats ont été récupérés sous la forme de deux listes : l’une
        pour les températures, l’autre pour les années :
        ```python
        t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
        annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
        ```

        Écrire la fonction `mini` qui prend en paramètres le tableau `releve` des relevés et le
        tableau `date` des dates et qui renvoie la plus petite valeur relevée au cours de la
        période et l’année correspondante.

        Exemple :
        ```python
        >>> mini(t_moy, annees)
        12.5, 2016
        ```

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



### Exercice 21.1 □
!!! example "Exercice 21.1"
    === "Énoncé" 
        Écrire une fonction python appelée `nb_repetitions` qui prend en paramètres un
        élément `elt` et une liste `tab` et renvoie le nombre de fois où l’élément apparaît dans la
        liste.

        Exemples :
        ```python
        >>> nb_repetitions(5,[2,5,3,5,6,9,5])
        3
        >>> nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R'])
        2
        >>> nb_repetitions(12,[1, '! ',7,21,36,44])
        0
        ```

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



### Exercice 22.1 □
!!! example "Exercice 22.1"
    === "Énoncé" 
        Écrire en langage Python une fonction `recherche` prenant comme paramètres une
        variable `a` de type numérique (`float` ou `int`) et un tableau `t` (type `list`) et qui
        renvoie le nombre d'occurrences de `a` dans `t`.

        Exemples :
        ```python
        >>> recherche(5,[])
        0
        >>> recherche(5,[-2, 3, 4, 8])
        0
        >>> recherche(5,[-2, 3, 1, 5, 3, 7, 4])
        1
        >>> recherche(5,[-2, 5, 3, 5, 4, 5])
        3
        ```

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



### Exercice 23.1 □
!!! example "Exercice 23.1"
    === "Énoncé" 
        L’occurrence d’un caractère dans un phrase est le nombre de fois où ce caractère est
        présent.

        Exemples :
        
        - l’occurrence du caractère ‘o’ dans ‘bonjour’ est 2 ;
        - l’occurrence du caractère ‘b’ dans ‘Bébé’ est 1 ;
        - l’occurrence du caractère ‘B’ dans ‘Bébé’ est 1 ;
        - l’occurrence du caractère ‘ ‘ dans ‘Hello world !’ est 2.

        On cherche les occurrences des caractères dans une phrase. On souhaite stocker ces
        occurrences dans un dictionnaire dont les clefs seraient les caractères de la phrase et
        les valeurs l’occurrence de ces caractères.


        Par exemple : avec la phrase 'Hello world !' le dictionnaire est le suivant :

        `{'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}`


        Écrire une fonction `occurence_lettres` prenant comme paramètre une variable
        `phrase` de type `str`. Cette fonction doit renvoyer un dictionnaire de type constitué des
        occurrences des caractères présents dans la phrase.

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



### Exercice 24.1 □
*identique au 18.1*
!!! example "Exercice 24.1"
    === "Énoncé" 
        Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
        un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt`
        dans `tab` si `elt` est dans `tab` et `-1` sinon.

        Exemples :
        ```python
        >>> recherche(1, [2, 3, 4])
        -1
        >>> recherche(1, [10, 12, 1, 56])
        2
        >>> recherche(50, [1, 50, 1])
        1
        >>> recherche(15, [8, 9, 10, 15])
        3
        ```

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



### Exercice 25.1 □
!!! example "Exercice 25.1"
    === "Énoncé" 
        Écrire une fonction `recherche` qui prend en paramètre un tableau de nombres entiers
        `tab`, et qui renvoie la liste (éventuellement vide) des couples d'entiers consécutifs
        successifs qu'il peut y avoir dans `tab`.

        Exemples :
        ```python
        >>> recherche([1, 4, 3, 5])
        []
        >>> recherche([1, 4, 5, 3])
        [(4, 5)]
        >>> recherche([7, 1, 2, 5, 3, 4])
        [(1, 2), (3, 4)]
        >>> recherche([5, 1, 2, 3, 8, -5, -4, 7])
        [(1, 2), (2, 3), (-5, -4)]
        ```

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



### Exercice 26.1 □
!!! example "Exercice 26.1"
    === "Énoncé" 
        Écrire une fonction `occurrence_max` prenant en paramètres une chaîne de caractères
        `chaine` et qui renvoie le caractère le plus fréquent de la chaîne. La chaine ne contient
        que des lettres en minuscules sans accent.
        On pourra s’aider du tableau

        `alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']`

        et du tableau `occurrence` de 26 éléments où l’on mettra dans `occurrence[i]` le
        nombre d’apparitions de `alphabet[i]` dans la chaine. Puis on calculera l’indice `k` d’un
        maximum du tableau `occurrence` et on affichera `alphabet[k]`.

        Exemple :
        ```python
        >>> ch='je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique’
        >>> occurrence_max(ch)
        ‘e’
        ```

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



### Exercice 27.1 □
!!! example "Exercice 27.1"
    === "Énoncé" 
        Écrire une fonction `moyenne` prenant en paramètres une liste d’entiers et qui renvoie la
        moyenne des valeurs de cette liste.

        Exemple :
        ```python
        >>> moyenne([10,20,30,40,60,110])
        45.0
        ```

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



### Exercice 28.1 □
!!! example "Exercice 28.1"
    === "Énoncé" 
        Dans cet exercice, un arbre binaire de caractères est stocké sous la forme d’un
        dictionnaire où les clefs sont les caractères des nœuds de l’arbre et les valeurs, pour
        chaque clef, la liste des caractères des fils gauche et droit du nœud.

        Par exemple, l’arbre

        ![image](data/img28_1.png){: .center width=40%}
        
        est stocké dans

        ```python
        a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
        'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
        'H':['','']}
        ```

        Écrire une fonction récursive `taille` prenant en paramètres un arbre binaire `arbre`
        sous la forme d’un dictionnaire et un caractère `lettre` qui est la valeur du sommet de
        l’arbre, et qui renvoie la taille de l’arbre à savoir le nombre total de nœud.
        On pourra distinguer les 4 cas où les deux « fils » du nœud sont `''`, le fils gauche
        seulement est `''`, le fils droit seulement est `''`, aucun des deux fils n’est `''`.

        Exemple :
        ```python
        >>> taille(a, ’F’)
        9
        ``` 

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




