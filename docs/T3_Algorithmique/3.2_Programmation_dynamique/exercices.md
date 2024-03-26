{{initexo(0)}}

!!! example "{{ exercice() }}"
    Exercice 1 du [sujet 0 - version B 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/bac_nsi_2024_sujet0b.pdf){. target="_blank"}

    {{
    correction(True,
    """
    ??? success \"Correction Q1.\" 
        ```python
           3
          1 2
         4 5 9
        3 6 2 1
        ```
    """
    )
    }}


    {{
    correction(True,
    """
    ??? success \"Correction Q2.\" 
        Un conduit de score de maximal est (par exemple) : 3-2-9-2 pour un score total de 16.
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q3.\" 
        Les différents conduits possibles sont :

        - 2-5-2
        - 2-5-3
        - 2-1-3
        - 2-1-9
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q4.\" 
        Pour une pyramide de $n$ niveaux, il va y avoir $n-1$ choix de direction (droite ou gauche). Cela revient donc à écrire un mot binaire composé de $n-1$ chiffres (0 ou 1).

        Or le nombre de mots binaires de longueur $n-1$ est égal à $2^{n-1}$ donc une pyramide de n niveaux comportera $2^{n-1}$ conduits.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q5.\" 
        D'après la formule précédente, le nombre de conduits évolue de manière exponentielle avec le nombre de niveaux de la pyramide. Pour une pyramide de taille 40, il sera de plusieurs milliards. Il est alors impossible de tous les étudier pour en extraire le conduit de score maximal. 
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q6.\" 
        ```python linenums='1'
        def score_max(i, j, p):
            if i == len(p) - 1:
                return p[len(p)-1][j]
            return p[i][j] + max(score_max(i+1, j, p), score_max(i+1, j+1, p)) 
        ```
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q7.\" 
        ```python linenums='1'
        def pyramide_nulle(n):
            pyr = []
            for k in range(1, n+1):
                niv = [0]*k
                pyr.append(niv)
            return pyr
        ```
        ou mieux :
        ```python linenums='1'
        def pyramide_nulle(n):
            return [[0]*k for k in range(1, n+1)]
        ```

    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q8.\" 
        ```python linenums='1', hl_lines='3 5 6 8-10'
        def prog_dyn(p):
            n = len(p)
            s = pyramide_nulle(n)
            # remplissage du dernier niveau
            for j in range(n):
                s[n-1][j] = p[n-1][j]
            # remplissage des autres niveaux
            for i in range(n-2, -1, -1):
                for j in range(len(s[i])):
                    s[i][j] = p[i][j] + max(s[i+1][j], s[i+1][j+1])
            # renvoie du score maximal
            return s[0][0]
        ```
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q9.\" 
        Les deux boucles imbriquées des lignes 8 et 9 sont responsables du coût quadratique : 
        
        - la première va engendrer $n-1$ itérations.
        - le nombre d'itérations de la deuxième dépend aussi de $n$

        Donc l'imbrication des deux boucles va provoquer un coût quadratique.
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q10.\" 
        On pourrait utiliser la mémoïsation pour éviter la redondance des calculs, par exemple en utilisant un dictionnaire de clés ```(i,j)``` pour stocker les ```score_max(i,j,p)```.
       
        Exemple de code (non demandé) :
        ```python linenums='1'
        memo = {}
        def score_max(i, j, p):
            if i == len(p) - 1:
                return p[len(p)-1][j]
            if (i, j) not in memo:
                memo[(i,j)] = p[i][j] + max(score_max(i+1, j, p), score_max(i+1, j+1, p))
            return memo[(i,j)]
        ```


        
    """
    )
    }}


!!! example "{{ exercice() }}"
    *Largement inspiré du sujet [24.2](https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2024/#__tabbed_48_1){. target="_blank"} de la BNS 2024.*

    On considère un tableau non vide de nombre entiers, positifs ou négatifs, et on souhaite déterminer
    la plus grande somme possible de ses éléments consécutifs.


    Par exemple, dans le tableau `[1, -2, 3, 10, -4, 7, 2, -5]`, la plus grande
    somme est 18 obtenue en additionnant les éléments 3, 10, -4, 7, 2.


    Pour cela, on va résoudre le problème par programmation dynamique. 

    Le problème sera résolu en 2 temps.

    Dans un premier temps, si on note `tab` le
    tableau considéré et `i` un indice dans ce tableau, on va chercher à déterminer la plus grande somme possible de ses éléments consécutifs se terminant à
    l’indice `i`.
    Voici la méthode :

    Si on connait la plus grande somme possible de ses éléments consécutifs se terminant à
    l’indice `i-1`, on peut déterminer la plus grande somme possible de ses éléments consécutifs
    se terminant à l’indice `i` :

    - soit on obtient une plus grande somme en ajoutant `tab[i]` à cette somme précédente ;
    - soit on commence une nouvelle somme à partir de `tab[i]`.

    Dans un deuxième temps, il suffira de parcourir le tableau pour chercher la somme maximale d'éléments consécutifs.


    Compléter la fonction `somme_max` ci-dessous qui réalise cet algorithme.

    ```python linenums='1'
    def somme_max(tab):
        n = len(tab)
        sommes_max = [0]*n
        sommes_max[0] = tab[0]
        # on calcule la plus grande somme se terminant en i
        for i in range(1,n):
            if ... + ... > ...: 
                sommes_max[i] = ... 
            else:
                sommes_max[i] = ... 
        # on en déduit la plus grande somme de celles-ci
        maximum = 0
        for i in range(1, n):
            if ... > ...: 
                maximum = i

        return sommes_max[...] 
    ```

    Exemples :

    ```python
    >>> somme_max([1, 2, 3, 4, 5])
    15
    >> somme_max([1, 2, -3, 4, 5])
    9
    >>> somme_max([1, 2, -2, 4, 5])
    10
    >>> somme_max([1, -2, 3, 10, -4, 7, 2, -5])
    18
    ``` 

    {{
    correction(False,
    """
    ??? success \"Correction\" 
        ```python linenums='1', hl_lines='7 8 10 14'
        def somme_max(tab):
            n = len(tab)
            sommes_max = [0]*n
            sommes_max[0] = tab[0]
            # on calcule la plus grande somme se terminant en i
            for i in range(1,n):
                if sommes_max[i-1] + tab[i] > tab[i]:
                    sommes_max[i] = sommes_max[i-1] + tab[i]
                else:
                    sommes_max[i] = tab[i]
            # on en déduit la plus grande somme de celles-ci
            maximum = 0
            for i in range(1, n):
                if sommes_max[i]  > sommes_max[maximum]:
                    maximum = i
            return sommes_max[maximum]
        ```
    """
    )
    }}