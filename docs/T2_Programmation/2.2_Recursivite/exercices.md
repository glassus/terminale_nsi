#Exercices

{{ initexo(0) }}


!!! example "{{ exercice() }}"
    Écrire une fonction récursive ```puissance``` qui prend en paramètres deux nombres ```x``` et ```n``` qui renvoie le nombre $x^n$.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def puissance(x, n):
            if n == 0:
                return 1
            else:
                return x * puissance(x, n-1)
        ```       
    """
    )
    }}




!!! example "{{ exercice() }} :heart: "

    On rappelle que le PGCD (plus grand diviseur commun de deux nombres) vérifie la propriété suivante : si la division euclidienne de $a$ par $b$ s'écrit $a = b \times q + r$, alors $pgcd(a,b)=pgcd(b,r)$. 

    Cette propriété est à la base de l'algorithme d'Euclide

    Exemple : $pgcd(24,18)=pgcd(18,6)=pgcd(6,0)$, donc $pgcd(24,18)=6$

    Écrire une fonction récursive ```pgcd``` qui prend en paramètres deux nombres ```a``` et ```b``` et qui renvoie leur PGCD.
    
    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def pgcd(a, b):
            if b == 0:
                return a
            else:
                return pgcd(b, a % b)
        ```    
    """
    )
    }}



!!! example "{{ exercice() }}"

    La [conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse){. target="_blank"}  (ou de Collatz) postule ceci :  

    *Prenons un nombre $n$ : si $n$ est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber sur le nombre 1.*

    **Q1.** Écrire une fonction récursive ```syracuse``` qui prend en paramètres une entier ```n``` et qui écrivant tous les termes de la suite de Syracuse commençant à ```n``` , et s'arrêtant (on l'espère...) à la valeur 1.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
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
    """
    )
    }}

    **Q2.** On appelle «temps de vol» le nombre d'étapes nécessaires avant de retomber sur 1. Modifier la fonction précédente afin qu'elle affiche le temps de vol pour tout nombre ```n```.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def syracuse(n, t=0):
            print(n)
            if n == 1:
                print('temps de vol :', t)
                return None
            if n % 2 == 0:
                syracuse(n // 2, t+1)
            else:
                syracuse(3*n + 1, t+1)
        ``` 
    """
        ) }}           
    



     

!!! example "{{ exercice() }}"
    Reproduire le dessin suivant, à l'aide du module ```turtle```.  

    ```turtle``` est un hommage au langage LOGO inventé par [Seymour Papert](https://fr.wikipedia.org/wiki/Seymour_Papert) au MIT à la fin des années 60.

    ![](data/carres_turtle.png){: .center width=40%}

    {{
    correction(True,
    """
    ??? success \"Correction\" 
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

        def trace(n, c):
            if n == 0 :
                return None
            else :
                base(c)
                c = c/(2**0.5)
                trace(n-1, c)
            
        trace(5, 200)
        ```        
    """
    )
    }}



!!! example "{{ exercice() }}"

    Proposer une nouvelle fonction récursive ```puissance_mod``` qui prend en paramètres deux nombres ```x``` et ```n``` et qui renvoie le nombre $x^n$. Pour optimiser la fonction déjà construite à l'exercice 1, utiliser le fait que :

    - si $n$ est pair, $a^n=(a \times a)^{n/2}$
    - sinon $a^n=a \times (a \times a)^{(n-1)/2}$

    
    {{
    correction(True,
    """
    ??? success \"Correction\" 
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
    """
    )
    }}
    

!!! example "{{ exercice() }}"
    Écrire un algorithme récursif ```dicho_recursive``` qui prend en paramètres une liste **triée** (par ordre croissant) ```lst``` et une valeur ```val```  et qui renvoie un booléen indiquant la présence ou non de la valeur ```val``` dans une liste ```lst```. 
    

    *Exemple d'utilisation :*

    ```python
    >>> lst = [2,4,5,5,7,9,11,15,16,18,19]
    >>> dicho_recursive(lst, 16)
    [2, 4, 5, 5, 7, 9, 11, 15, 16, 18, 19]
    [9, 11, 15, 16, 18, 19]
    [16, 18, 19]
    [16]
    True
    >>> dicho_recursive(lst, 6)
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

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def dicho_recursive(lst, val):
            print(lst) # pour voir la taille de la liste diminuer
            if len(lst) == 1:   # cas de base
                return lst[0] == val:
            else :              # cas récursif
                ind_milieu = len(lst)//2
                if lst[ind_milieu] > val:
                    return recherche(lst[:ind_milieu], val)
                else:
                    return recherche(lst[ind_milieu:], val)
        ```       
    """
    )
    }}


!!! example "{{ exercice() }}"

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

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def hanoi(n, depart, inter, arrivee):
            ''' n : nombre d'assiettes dans la pile
            # depart : la pile de départ('A', 'B' ou 'C')
            # inter : la pile intermédaire('A', 'B' ou 'C')
            # arrivee : la pile d'arrivée ('A', 'B' ou 'C') '''

            if n == 1 :
                print(depart + ' vers ' + arrivee)
            else :
                hanoi(n-1, depart, arrivee, inter) 
                print(depart + ' vers ' + arrivee)
                hanoi(n-1, inter, depart, arrivee)

        hanoi(5, 'A', 'B', 'C')
        ```        
    """
    )
    }}
    

    


!!! example "{{ exercice() }}"

    Cet exercice a pour objectif le tracé du flocon de Von Koch.
    ![](data/floc.png){: .center width=60%}

    !!! info "Les fractales"
        Ce flocon est une structure [fractale](https://fr.wikipedia.org/wiki/Fractale){. target="_blank"}, au même titre que le superbe [ensemble de Mandelbrot](https://mandelbrot.site/){. target="_blank"}, dont vous pouvez trouver une implémentation en Pygame [ici](data/mandelbrot_pygame.py){. target="_blank"}.

    L'idée est de répéter de manière récursive la transformation ci-dessous : chaque segment de longueur ```l``` donne naissance à 4 segments de longueur ```l/3```, en construisant une pointe de triangle équilatéral sur le deuxième tiers du segment.

    ![](data/ex2.png){: .center width=60%}



    **Q1.** Créer une fonction récursive ```floc(n, l)``` qui trace à une «profondeur» ```n``` un segment de longueur ```l```.
    ![](data/ex3b.png){: .center width=60%}
    **Indications**

    - l'instruction de tracé n'a lieu que quand ```n``` vaut 0.
    - l'étape ```n``` fait 4 appels successifs à l'étape ```n-1```.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
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
        ```    
    """
    )
    }}

    **Q2.** Créer une fonction ```triangle(n, l)``` qui trace le flocon complet.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
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
    """
    )
    }}
        



!!! example "{{ exercice() }}"

    1. [Exercice 43.2 de la BNS 2025](https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2025/#exercice-432){. target="_blank"}
    2. Application sur Capytale à retrouver [ici](https://capytale2.ac-paris.fr/web/c/ffb5-785788/mlc){. target="_blank"} 

    ![image](data/diffusion.png){: .center}

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def propager(grid, i, j, color):
            if grid[i,j].green != 180:
                return None 

            grid[i,j].green = color

            if (i-1) >= 0:
                propager(grid, i-1, j, color)

            if (i+1) < n:
                propager(grid, i+1, j, color)

            if (j-1) >= 0:
                propager(grid, i, j-1, color)

            if (j+1) < n : 
                propager(grid, i, j+1, color)


        grid = initgrid()
        propager(grid,3,3,0)
        grid.show()
        ```        
    """
    )
    }}


!!! example "{{ exercice() }}"
    Exercice 4 du sujet [Amérique du Nord J1 2022](../../T6_Annales/data/2022/2022_Amerique_Nord_J1.pdf){. target="_blank"}

    {{
    correction(True,
    """
    ??? success \"Correction Q1.a.\" 
        Proposition 3        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q1.b.\" 
        ```txt[0]``` vaut 'b'  
        ```txt[taille-1]``` vaut 'r'  
        ```interieur``` vaut 'onjou'          
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q2.\" 
        ```python linenums='1'
        def test_palindrome():
            assert palindrome('kayak') == True
            assert palindrome('canoe') == False  
            printt("tests ok") 
        ```
        On teste les deux cas possibles.        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q3.\" 
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
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q4.a.\" 
        ```python linenums='1'
        def complementaire(txt):
            comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
            sol = ''
            for c in txt:
                sol += comp[c]
            return sol
        ```         
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q4.b\" 
        'GATCGTCTAGCA' n'est pas un palindrome donc 'GATCGT' n'est pas palindromique.        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q4.c\" 
        ```python linenums='1'
        def est_palindromique(txt):
            txt_total = txt + complementaire(txt)
            return palindrome(txt_total)
        ```        
    """
    )
    }}





!!! example "{{ exercice() }}"
    Exercice 1 du sujet [Centres Étrangers J2 2022](../../T6_Annales/data/2022/2022_Centres_Etrangers_J2.pdf){. target="_blank"}

    {{
    correction(False,
    """
    ??? success \"Correction Q1.a.\" 
        ```f(5)``` affichera :
        ```5
        4
        3
        2
        1
        Partez!``        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q1.b.\" 
        On dit que cette fonction est récursive car elle s'appelle elle-même à l'intérieur de sa propre définition.        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction  Q2.a.\" 
        ```python linenums='1'
        def ajouter(s, liste):
            res = []
            for m in liste:
                res.append(s + m)
            return res
        ```        
    """
    )
    }}
    
    {{
    correction(False,
    """
    ??? success \"Correction Q2.b.\" 
        La commande renvoie :
        ```python
        ['ba', 'bb', 'bc']
        ```        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q2.c.\" 
        La commande renvoie :
        ```python
        ['a']
        ```        
    """
    )
    }}

    {#
    La question 3. est difficile, vous pouvez vous aider du code ci-dessous :


    ```python
    def ajouter(s, liste):
        res = []
        for m in liste:
            res.append(s + m)
        return res


    def produit(s, n):
        if n == 0:
            return [""]
        else:
            res = []
            for i in range(len(s)):
                res = res + ajouter(s[i], produit(s, n-1))
            return res


    ```
    #}


    {{
    correction(False,
    """
    ??? success \"Correction Q3.a.\" 
        Comme ```n``` vaut 0, on est dans le cas de base et donc la commande renvoie ```[\"\"]```.

        ```[\"\"]``` **n'est pas** une liste vide, car elle contient un élément (une chaine de caractères vide). La liste vide est ```[]```.        
    """
    )
    }}
        
    {{
    correction(False,
    """
    ??? success \"Correction Q3.b.\" 
        ```produit('ab', 1) ``` renvoie  ```['a', 'b']```.        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q3.c.\" 
        ```produit('ab', 2) ``` renvoie  ```['aa', 'ab', 'ba', 'bb']```.           
    """
    )
    }}

        

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
        - étape 3 : 27 appels

        Il y a donc 39 appels au total.
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
