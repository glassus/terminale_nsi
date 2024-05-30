#Exercices

{{ initexo(0) }}


!!! example "{{ exercice() }}"
    === "Énoncé"
        Écrire une fonction récursive ```puissance(x, n)``` qui calcule le nombre $x^n$.
    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        def puissance(x, n):
            if n == 0:
                return 1
            else:
                return x * puissance(x, n-1)
        ```
        "
        ) }}



!!! example "{{ exercice() }} :heart: "
    === "Énoncé"
        On rappelle que le PGCD (plus grand diviseur commun de deux nombres) vérifie la propriété suivante : si la division euclidienne de $a$ par $b$ s'écrit $a = b \times q + r$, alors $pgcd(a,b)=pgcd(b,r)$. 

        Cette propriété est à la base de l'algorithme d'Euclide

        Exemple : $pgcd(24,18)=pgcd(18,6)=pgcd(6,0)$, donc $pgcd(24,18)=6$

        Écrire un algorithme récursif ```pgcd(a,b)```.
    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        def pgcd(a, b):
            if a%b == 0:
                return b
            else:
                return pgcd(b, a%b)
        ```
        "
        ) }}



!!! example "{{ exercice() }}"
    === "Énoncé"
        La conjecture de Syracuse (ou de Collatz) postule ceci :  

        *Prenons un nombre $n$ : si $n$ est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber sur le nombre 1.*

        1. Proposer un programme récursif ```syracuse(n)``` écrivant tous les termes de la suite de Syracuse, s'arrêtant (on l'espère) à la valeur 1.
        2. On appelle «temps de vol» le nombre d'étapes nécessaires avant de retomber sur 1. Modifier la fonction précédente afin qu'elle affiche le temps de vol pour tout nombre ```n```.

    === "Correction"
        {{ correction(True,
        "
        1.

        ```python linenums='1'
        def syracuse(n):
            print(n)
            if n == 1:
                return None
            if n % 2 == 0:
                return syracuse(n // 2)
            else:
                return syracuse(3*n + 1)
        ```

        Remarque : comme notre fonction ```syracuse``` ne renvoie pas de valeur numérique (elle ne fait qu'afficher une valeur), le ```return``` du test de parité est en fait inutile.

        Mais le ```return``` du cas de base est lui primordial pour que le code s'arrête !  

        ```python linenums='1'
        def syracuse(n):
            print(n)
            if n == 1:
                return None
            if n % 2 == 0:
                syracuse(n // 2)
            else:
                syracuse(3*n + 1)
        ```
        2.
        ```python linenums='1'
        def syracuse(n, t=0):
            print(n)
            t += 1
            if n == 1:
                print('temps de vol :', t)
                return None
            if n % 2 == 0:
                syracuse(n // 2, t)
            else:
                syracuse(3*n + 1, t)
        ``` 
        "
        ) }}        

!!! example "{{ exercice() }}"
    === "Énoncé"
        Reproduire le dessin suivant, à l'aide du module ```turtle```.  

        ```turtle``` est un hommage au langage LOGO inventé par [Seymour Papert](https://fr.wikipedia.org/wiki/Seymour_Papert) au MIT à la fin des années 60.

        ![](data/carres_turtle.png){: .center width=40%}

    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        from turtle import *
        def carre(c):
            for k in range(4):
                forward(c)
                right(90)

        def base(c):
            carre(c)
            forward(c/2)
            right(45)

        def trace(c, n):
            if n == 0 :
                return None
            else :
                base(c)
                c = c/(2**0.5)
                trace(c, n-1)
            
        trace(200, 5)
        ```
        "
        ) }}


!!! example "{{ exercice() }}"
    === "Énoncé"
        Proposer une nouvelle fonction récursive ```puissance_mod(x, n)``` qui calcule le nombre $x^n$. Pour optimiser la fonction déjà construite à l'exercice 1, utiliser le fait que :

        - si $n$ est pair, $a^n=(a \times a)^{n/2}$
        - sinon $a^n=a \times (a \times a)^{(n-1)/2}$

    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        def puissance_mod(x, n):
            if n == 0 :
                return 1
            else :
                if n % 2 == 0:
                    return puissance_mod(x*x, n//2)
                else :
                    return x * puissance_mod(x*x, (n-1)//2)
        ```
        "
        ) }}       

!!! example "{{ exercice() }}"
    === "Énoncé"
        Écrire un algorithme récursif ```recherche(lst, val)``` qui recherche la présence de la valeur ```val``` dans une liste **triée** (par ordre croissant) ```lst```. 
        
        Cette fonction doit renvoyer un booléen.

        *Exemple d'utilisation :*

        ```python
        >>> lst = [2,4,5,5,7,9,11,15,16,18,19]
        >>> recherche(lst, 16)
        [2, 4, 5, 5, 7, 9, 11, 15, 16, 18, 19]
        [9, 11, 15, 16, 18, 19]
        [16, 18, 19]
        [16]
        True
        >>> recherche(lst, 6)
        [2, 4, 5, 5, 7, 9, 11, 15, 16, 18, 19]
        [2, 4, 5, 5, 7]
        [5, 5, 7]
        [5, 7]
        [5]
        False
        
        ```

        _Aide :_
        
        Les techniques de *slicing* (hors-programme) permettent de couper une liste en deux : 
        ```python
        >>> lst = [10, 12, 15, 17, 18, 20, 22]
        >>> lst[:3]
        [10, 12, 15]
        >>> lst[3:]
        [17, 18, 20, 22]
        ``` 

    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        def recherche(lst, val):
            print(lst) # pour voir la taille de la liste diminuer
            if len(lst) == 1:  #cas de base
                if lst[0] == val:
                    return True
                else:
                    return False
            else :              #cas récursif
                ind_milieu = len(lst)//2
                if lst[ind_milieu] > val:
                    return recherche(lst[:ind_milieu], val)
                else:
                    return recherche(lst[ind_milieu:], val)
        ```
        "
        ) }}       
        

!!! example "{{ exercice() }}"
    === "Énoncé"
        On considère le jeu des **Tours de Hanoï**.
        Le but est de faire passer toutes les assiettes de A vers C, sachant qu'une assiette ne peut être déposée que sur une assiette de diamètre inférieur.
        ![](data/hanoi0.png){: .center width=60%}

        Une version jouable en ligne peut être trouvée [ici](https://www.mathsisfun.com/games/towerofhanoi.html){. target="_blank"}.

        1. S'entraîner et essayer d'établir une stratégie de victoire.
        2. Observer les images ci-dessous :
        ![](data/hanoi1.png){: .center width=60%}
        ![](data/hanoi2.png){: .center width=60%}
        ![](data/hanoi3.png){: .center width=60%}
        ![](data/hanoi4.png){: .center width=60%}


        Écrire une fonction récursive ```hanoi(n, depart, inter, arrivee)``` qui donnera la suite d'instructions (sous la forme " A vers C") pour faire passer une pile de taille n de ```depart```  vers ```arrivee```  en prenant ```inter```  comme intermédiaire.

    === "Correction"
    
        ```python linenums='1'
        def hanoi(n, depart, inter, arrivee):
            """ n : nombre d'assiettes dans la pile
            # depart : la pile de départ("A", "B" ou "C")
            # inter : la pile intermédaire("A", "B" ou "C")
            # arrivee : la pile d'arrivée ("A", "B" ou "C") """

            if n == 1 :
                print(depart + " vers " + arrivee)
            else :
                hanoi(n-1, depart, arrivee, inter) 
                print(depart + " vers " + arrivee)
                hanoi(n-1, inter, depart, arrivee)

        hanoi(5, "A", "B", "C")
        ```
    


!!! example "{{ exercice() }}"
    === "Énoncé"
        Cet exercice a pour objectif le tracé du flocon de Von Koch.
        ![](data/floc.png){: .center width=60%}


        L'idée est de répéter de manière récursive la transformation ci-dessous : chaque segment de longueur ```l``` donne naissance à 4 segments de longueur ```l/3```, en construisant une pointe de triangle équilatéral sur le deuxième tiers du segment.

        ![](data/ex2.png){: .center width=60%}



        1) Créer une fonction récursive ```floc(n, l)``` qui trace à une «profondeur» ```n``` un segment de longueur ```l```.
        ![](data/ex3b.png){: .center width=60%}
        **Indications**

        - l'instruction de tracé n'a lieu que quand ```n``` vaut 0.
        - l'étape ```n``` fait 4 appels successifs à l'étape ```n-1```.

        2) Créer une fonction ```triangle(n, l)``` qui trace le flocon complet.

    === "Correction"
        
        ```python linenums='1'
        from turtle import *

        def floc(n, l):
            if n == 0:
                forward(l)
            else:
                floc(n-1,l/3)
                left(60)
                floc(n-1,l/3)
                right(120)
                floc(n-1,l/3)
                left(60)
                floc(n-1,l/3)
                

        speed(0)

        def triangle(n,l):
            for _ in range(3):
                floc(n,l)
                right(120)
                
        triangle(5,400)

        ```
        



!!! example "{{ exercice() }}"
    === "Énoncé"
        1. [Exercice 04.2 de la BNS 2022](https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#exercice-042){. target="_blank"}
        2. Application sur Capytale à retrouver [ici](https://capytale2.ac-paris.fr/web/c/ffb5-785788/mlc){. target="_blank"} 

        ![image](data/diffusion.png){: .center}
        
    === "Correction"
        {#
        ```python linenums='1'
        def propager(grid, i, j, color):
            if grid[i,j].green == 0:
                return None # 

            grid[i,j].green = color

            # l'élément en haut fait partie de la composante
            if ((i-1) >= 0 and grid[i-1,j].green == 180):
                propager(grid, i-1, j, color)

            # l'élément en bas fait partie de la composante
            if ((i+1) < n and grid[i+1,j].green == 180):
                propager(grid, i+1, j, color)

            # l'élément à gauche fait partie de la composante
            if ((j-1) >= 0 and grid[i,j-1].green == 180):
                propager(grid, i, j-1, color)

            # l'élément à droite fait partie de la composante
            if ((j+1) < n and grid[i,j+1].green == 180): # 
                propager(grid, i, j+1, color)


        grid = initgrid()
        propager(grid,0,3,0)
        grid.show()
        ```
        #}


!!! example "{{ exercice() }}"
    Exercice 4 du sujet [Amérique du Nord J1](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Amerique_Nord_J1.pdf){. target="_blank"}

    ??? tip "correction Q1.a."
        Proposition 3

    ??? tip "correction Q1.b."
        ```txt[0]``` vaut 'b'  
        ```txt[taille-1]``` vaut 'r'  
        ```interieur``` vaut 'onjou'  


    ??? tip "correction Q2."
        ```python linenums='1'
        def test_palindrome():
            assert palindrome("kayak") == True
            assert palindrome("canoe") == False   
        ```
        On teste les deux cas possibles.

    ??? tip "correction Q3."
        ```python linenums='1'
        def palindrome_imperatif(txt):
            if len(txt) < 2:
                return True
            i = 0
            j = len(txt)-1
            while i<j:
                if txt[i] != txt[j]:
                    return False
                i += 1
                j -= 1
            return True
        ```

    ??? tip "correction Q4.a."
        ```python linenums='1'
        def complementaire(txt):
            comp = {"A":"T", "T":"A", "G":"C", "C":"G"}
            sol = ""
            for c in txt:
                sol += comp[c]
            return sol
        ``` 

    ??? tip "correction Q4.b"
        "GATCGTCTAGCA" n'est pas un palindrome donc "GATCGT" n'est pas palindromique.

    ??? tip "correction Q4.c"
        ```python linenums='1'
        def est_palindromique(txt):
            txt_total = txt + complementaire(txt)
            return palindrome(txt_total)
        ```



!!! example "{{ exercice() }}"
    Exercice 1 du sujet [Centres Étrangers J2 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Centres_Etrangers_J2.pdf){. target="_blank"}

    ??? tip "correction Q1.a."
        ```f(5)``` affichera :
        ```5
        4
        3
        2
        1
        Partez!``

    ??? tip "Correction Q1.b."
        On dit que cette fonction est récursive car elle s'appelle elle-même à l'intérieur de sa propre définition.

    ??? tip "Correction Q2.a."
        ```python linenums='1'
        def ajouter(s, liste):
            res = []
            for m in liste:
                res.append(s + m)
            return res
        ```
    ??? tip "Correction Q2.b."
        La commande renvoie :
        ```python
        ['ba', 'bb', 'bc']
        ```
    
    ??? tip "Correction Q2.c."
        La commande renvoie :
        ```python
        ['a']
        ```
         
    ??? tip "Correction Q3.a."
        Comme ```n``` vaut 0, on est dans le cas de base et donc la commande renvoie ```[""]```.

        ```[""]``` **n'est pas** une liste vide, car elle contient un élément (une chaine de caractères vide). La liste vide est ```[]```.

    ??? tip "Correction Q3.b."
        ```produit("ab", 1) ``` renvoie  ```['a', 'b']```.

    ??? tip "Correction Q3.c."
        ```produit("ab", 2) ``` renvoie  ```['aa', 'ab', 'ba', 'bb']```.    

        

!!! example "{{ exercice() }} <i id="ex1J2AN2024"></i>"

    Exercice 1 du [sujet Amérique du Nord J2 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/24-NSIJ2AN1.pdf){. target="_blank"}    

    {{
    correction(False,
    """
    ??? success \"Correction Q1\" 
        ```python linenums='1'
        def echange(tab, i, j):
            temp = tab[i]
            tab[i] = tab[j]
            tab[j] = temp       
        ``` 
    """
    )
    }}
    
    {{
    correction(False,
    """
    ??? success \"Correction Q2\" 
        ```python linenums='1' hl_lines='6-8'
        def triStooge(tab, i, j):
            if tab[i] > tab[j]:
                echange(tab, i, j)
            if j - i > 1:
                k = (j - i + 1) // 3
                triStooge(tab, i, j-k)
                triStooge(tab, i+k, j)
                triStooge(tab, i, j-k)
        ``` 
    """
    )
    }}




    {{
    correction(False,
    """
    ??? success \"Correction Q3\" 
        Cet algorithme est récursif car aux lignes 6, 7 et 8, la fonction s'appelle elle-même.
    """
    )
    }}
    
    {{
    correction(False,
    """
    ??? success \"Correction Q4\" 
        ```k``` vaut ```(5 - 0 + 1) // 3```, donc ```k``` vaut 2. 
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q5\" 
        - étape 1 : 3 appels
        - étape 2 : 9 appels
        - étape 3 : 17 appels

        Il y a donc 29 appels au total.
    """
    )
    }}
    
    {{
    correction(False,
    """
    ??? success \"Correction Q6\" 
        - case 1 : ```triStooge(A,1,3)``` 
        - case 2 : ```triStooge(A,2,3)```
        - case 3 : ```triStooge(A,0,3)```        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q7\" 

        Correction probable, mais cette question est incompréhensible...

        | Appel | Valeur de A avant l'appel | Valeur de A après l'appel |
        |:---:|:---:|:---:|
        | ```triStooge(A,0,3) ```  | [5, 6, 4, 2] | [2, 6, 4, 5] |
        |  ```triStooge(A,0,2) ```| [2, 6, 4, 5] | [2, 4, 6, 5] |
        |  ```triStooge(A,1,3) ```| [2, 4, 6, 5]| [2, 4, 5, 6]  |
        |  ```triStooge(A,0,2) ```| [2, 4, 5, 6] | [2, 4, 5, 6]   |
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q8\" 
        Nous connaissons (par exemple) le tri par sélection, dont l'ordre est en $n^2$. 

        Comme $2 < \\frac{8}{3}$, on en déduit que le tri par sélection a un coût meilleur que le tri de Stooge. 
    """
    )
    }}

{#
??? quote "Bibliographie"
    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
    - Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.
#}
