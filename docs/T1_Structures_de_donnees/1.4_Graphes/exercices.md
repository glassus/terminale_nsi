{{initexo(0)}}

!!! example "{{ exercice() }}"
    Exercice 3 du [sujet 0 version A - 2024](https://glassus.github.io/terminale_nsi/T6_Annales/data/2024/bac_nsi_2024_sujet0a.pdf){. target="_blank"}

    {{
    correction(False,
    """
    ??? success \"Correction Q1.\" 
        ![image](data/0A_Q1.png){: .center}
        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q2.\" 
        Le chemin le plus court est A-E-D (10 km).
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q3.\" 
        La matrice d'adjacence de G1 est :
        $\\pmatrix{
        0 & 4 & 0 & 0 & 4 & 0 & 0  \\\\
        4 & 0 & 0 & 0 & 0 & 7 & 5  \\\\ 
        0 & 0 & 0 & 4 & 8 & 0 & 0  \\\\
        0 & 0 & 4 & 0 & 6 & 8 & 0  \\\\ 
        0 & 5 & 0 & 0 & 0 & 3 & 0  \\\\
        0 & 7 & 0 & 8 & 0 & 0 & 3  \\\\ 
        0 & 5 & 0 & 0 & 0 & 3 & 0  \\\\
        }$  
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q4.\" 
        ```python linenums='1'
        G2 = {'A': ['B', 'C', 'H'],
              'B': ['A', 'I'],
              'C': ['A', 'D', 'E'],
              'D': ['C', 'E'],
              'E': ['C', 'D', 'G'],
              'F': ['G', 'I'],
              'G': ['E', 'F', 'H'],
              'H': ['A', 'G', 'I'],
              'I': ['B', 'F', 'H']
             }
        ```
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q5.\" 
        Le parcours en largeur de ce graphe donne A-B-C-H-I-D-E-G-F.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q6.\" 
        La fonction ```cherche_itineraires``` s'appelle elle-même, elle est donc récursive.
    """
    )
    }}
    {{
    correction(False,
    """
    ??? success \"Correction Q7.\" 
        La fonction ```cherche_itineraires``` sert à remplir la liste ```tab_itineraires``` (initialement vide) avec tous les chemins (uniques) partant de ```start``` et allant à ```end```. 
    """
    )
    }}

    ??? tip "Code pour tester la Q8."
        ```python linenums='1'
        G2 = {'A': ['B', 'C', 'H'],
            'B': ['A', 'I'],
            'C': ['A', 'D', 'E'],
            'D': ['C', 'E'],
            'E': ['C', 'D', 'G'],
            'F': ['G', 'I'],
            'G': ['E', 'F', 'H'],
            'H': ['A', 'G', 'I'],
            'I': ['B', 'F', 'H']
            }

        tab_itineraires = []
        def cherche_itineraires(G, start, end, chaine=[]):
            chaine = chaine + [start]
            if start == end:
                return chaine
            for u in G[start]:
                if u not in chaine:
                    nchemin = cherche_itineraires(G, u, end, chaine)
                    if len(nchemin) != 0:
                        tab_itineraires.append(nchemin)
            return []


        def itineraires_court(G, dep, arr):
            cherche_itineraires(G, dep, arr)
            tab_court = ...
            mini = float('inf')
            for v in tab_itineraires:
                if len(v) <= ...:
                    mini = ...
            for v in tab_itineraires:
                if len(v) == mini:
                    tab_court.append(...)
            return tab_court        
        ```

    {{
    correction(False,
    """
    ??? success \"Correction Q8.\" 
        ```python linenums='1' hl_lines='30 31 27 34'
        G2 = {'A': ['B', 'C', 'H'],
            'B': ['A', 'I'],
            'C': ['A', 'D', 'E'],
            'D': ['C', 'E'],
            'E': ['C', 'D', 'G'],
            'F': ['G', 'I'],
            'G': ['E', 'F', 'H'],
            'H': ['A', 'G', 'I'],
            'I': ['B', 'F', 'H']
            }

        tab_itineraires = []
        def cherche_itineraires(G, start, end, chaine=[]):
            chaine = chaine + [start]
            if start == end:
                return chaine
            for u in G[start]:
                if u not in chaine:
                    nchemin = cherche_itineraires(G, u, end, chaine)
                    if len(nchemin) != 0:
                        tab_itineraires.append(nchemin)
            return []


        def itineraires_court(G, dep, arr):
            cherche_itineraires(G, dep, arr)
            tab_court = []
            mini = float('inf')
            for v in tab_itineraires:
                if len(v) <= mini:
                    mini = len(v)
            for v in tab_itineraires:
                if len(v) == mini:
                    tab_court.append(v)
            return tab_court
        

        ```
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q9.\" 
        Le problème vient de la variable globale ```tab_itineraires```.
        
        - Après l'exécution de la commande ```itineraires_court(G2, 'A', 'E')```,  ```tab_itineraires``` contient tous les chemins de A à E.
        - Si le programme n'est pas re-exécuté, l'enchainement avec la commande ```itineraires_court(G2, 'A', 'F')``` va venir **rajouter** à la liste ```tab_itineraires``` tous les chemins de A à F.
        - Lors de la recherche du trajet minimum, les trajets testés seront donc à la fois les trajets de A à F mais aussi de A à E : on peut donc potentiellement avoir une réponse erronnée.


        Pour éviter cela, on pourrait faire ceci (non demandé) :

        ```python linenums='1'
        def cherche_itineraires(G, start, end, chaine=[]):
            tab_itineraires = []
            def cherche(G, start, end, chaine=[]):
                chaine = chaine + [start]
                if start == end:
                    return chaine
                for u in G[start]:
                    if u not in chaine:
                        nchemin = cherche(G, u, end, chaine)
                        if len(nchemin) != 0:
                            tab_itineraires.append(nchemin)
                return []
            cherche(G, start, end, chaine=[])
            return tab_itineraires


        def itineraires_court(G, dep, arr):
            tab_itineraires = cherche_itineraires(G, dep, arr)
            tab_court = []
            mini = float('inf')
            for v in tab_itineraires:
                if len(v) <= mini:
                    mini = len(v)
            for v in tab_itineraires:
                if len(v) == mini:
                    tab_court.append(v)
            return tab_court
        ```
    """
    )
    }}


!!! example "{{ exercice() }}"
    *extrait de la BNS 2024*

    On considère dans cet exercice un graphe orienté représenté sous forme de listes d’adjacence.

    On suppose que les sommets sont numérotés de `0` à `n-1`.

    Par exemple, le graphe suivant :

    ![image](../../T6_6_Epreuve_pratique/data2024/graph2.png){: .center}

    est représenté par la liste d’adjacence suivante :

    ```python
    adj = [[1, 2], [2], [0], [0]]
    ```

    Écrire une fonction `voisins_entrants(adj, x)` qui prend en paramètre le graphe
    donné sous forme de liste d’adjacence et qui renvoie une liste contenant les voisins entrants
    du sommet `x`, c’est-à-dire les sommets `y` tels qu’il existe une arête de `y` vers `x`.

    Exemples :

    ```python
    >>> voisins_entrants([[1, 2], [2], [0], [0]], 0)
    [2, 3]
    >>> voisins_entrants([[1, 2], [2], [0], [0]], 1)
    [0]
    ```

    {{
    correction(False,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def voisins_entrants(adj, x):
            vois = []
            for i in range(len(adj)):
                if x in adj[i]:
                    vois.append(i)
            return vois        
        ```

    """
    )
    }}

!!! example "{{ exercice() }}"
    Dans cet exercice, on considère un graphe non orienté représenté sous forme de listes
    d’adjacence. On suppose que les sommets sont numérotés de 0 à n-1.

    Ainsi, le graphe suivant:

    ![image](../../T6_6_Epreuve_pratique/data2024/graph1.png){: .center}


    sera représenté par la liste d’adjacence suivante:

    `adj = [[1, 2], [0, 3], [0], [1], [5], [4]]`

    On souhaite déterminer les sommets accessibles depuis un sommet donné dans le graphe.
    Pour cela, on va procéder à un parcours en profondeur du graphe.

    Compléter la fonction suivante.

    ```python linenums='1'
    def parcours(adj, x, acc):
        '''Réalise un parcours en profondeur récursif
        du graphe donné par les listes d'adjacence adj 
        depuis le sommet x en accumulant les sommets
        rencontrés dans acc'''
        if x ...: 
            acc.append(x)
            for y in ...: 
                parcours(adj, ...) 

    def accessibles(adj, x):
        '''Renvoie la liste des sommets accessibles dans le
        graphe donné par les listes d'adjacence adj depuis
        le sommet x.'''
        acc = []
        parcours(adj, ...) 
        return acc
    ```

    Exemples :
    ```python
    >>> accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0)
    [0, 1, 2, 3]
    >>> accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4)
    [4, 5]    
    ```

    {{
    correction(False,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        adj = [[1, 2], [0, 3], [0], [1], [5], [4]]

        def parcours(adj, x, acc):
            '''Réalise un parcours en profondeur récursif
            du graphe donné par les listes d'adjacence adj
            depuis le sommet x en accumulant les sommets
            rencontrés dans acc'''
            if x not in acc:
                acc.append(x)
                for y in adj[x]:
                    parcours(adj, y, acc)

        def accessibles(adj, x):
            '''Renvoie la liste des sommets accessibles dans le
            graphe donné par les listes d'adjacence adj depuis
            le sommet x.'''
            acc = []
            parcours(adj, x, acc)
            return acc
        ```
    """
    )
    }}
