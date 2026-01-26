{{initexo(0)}}

!!! example "{{ exercice() }}"

    Exercice 4 du sujet [Amérique du Sud J2 2022](../../T6_Annales/data/2022/2022_Amerique_Sud_J2.pdf){. target="_blank"}

    {{
    correction(True,
    """
    ??? success \"Correction Q1.a\" 
        ```python
        from math import sqrt
        ```        
    """
    )
    }}


    !!! note "Q1.b : tester son code"
        ```python
        >>> distance_points((3, 5), (7, 4))
        4.123105625617661
        ``` 


    {{
    correction(True
    """
    ??? success \"Correction Q1.b\" 
        ```python linenums='1'
        def distance_points(a, b):
            return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
        ```        
    """
    )
    }}

    !!! note "Q2 : tester son code"
        ```python
        >>> distance((8, 3), (5, 6), (3, 7))
        1.3416407864998738
        >>> distance((8, 3), (5, 6), (5, 6))
        4.242640687119285
        ``` 

    {{
    correction(False,
    """
    ??? success \"Correction Q2.\" 
        ```python linenums='1'
        def distance(p, a, b):
            if a == b:
                return distance_points(p, a)
            else:
                return distance_point_droite(p, a, b)
        ```        
    """
    )
    }}


    !!! note "Q3 : tester son code"

        Fonction ```distance_point_droite``` :
        ```python linenums='1'
        def distance_point_droite(p, a, b):
            if b[0] == a[0]:
                return abs(p[0]-a[0])
            m = (b[1] - a[1]) / (b[0] - a[0])
            od = a[1] - m*a[0]
            xm = (p[0]*(b[0]-a[0])+(p[1]-od)*(b[1]-a[1])) / (b[0]-a[0] + m*(b[1]-a[1]))
            ym = m*xm + od
            return distance_points(p, (xm, ym))  

        ``` 

        ```python
        >>> le_plus_loin([(1, 3), (2, 7), (3, 4), (5, 3)])
        (1, 4.0)
        ``` 


    {{
    correction(False,
    """
    ??? success \"Correction Q3.\" 
        ```python linenums='1' hl_lines='8 10-13'
        def le_plus_loin(ligne):
            n = len(ligne)
            deb = ligne[0]
            fin = ligne[n-1]
            dmax = 0
            indice_max = 0
            for idx in range(1, n-1):
                p = ligne[idx]
                d = distance(p, deb, fin)
                if d > dmax:
                    dmax = d
                    indice_max = idx
            return (indice_max, dmax)
        ```        
    """
    )
    }}

    !!! note "Q4 : tester son code"
        ```python
        >>> extrait([(1, 3), (2, 7), (3, 4), (4, 4), (5, 3), (6, 2)], 1, 4)
        [(2, 7), (3, 4), (4, 4), (5, 3)]
        ``` 


    {{
    correction(False,
    """
    ??? success \"Correction Q4.\" 
        ```python linenums='1'
        def extrait(tab, i, j):
            ext = []
            for k in range(i, j+1):
                ext.append(tab[k])
            return ext
        ``` 

        ou 

        ```python linenums='1'
        def extrait(tab, i, j):
            return [tab[k] for k in range(i, j+1)]
        ```     

        ou 

        ```python linenums='1'
        def extrait(tab, i, j):
            return tab[i:j+1]
        ``` 

    """
    )
    }}

    !!! note "Q5 : tester son code"
        ```python
        >>> simplifie([(1, 3), (2, 7), (3, 4), (4, 4), (5, 3), (6, 2)], 3)
        [(1, 3), (2, 7), (3, 4), (6, 2)]
        ``` 

        ![image](data/geog.png){: .center}
        

    {{
    correction(False,
    """
    ??? success \"Correction Q5.\" 
        ```python linenums='1' hl_lines='4 8 10-11'
        def simplifie(ligne, seuil):
            n = len(ligne)
            if n <= 2:
                return ligne
            else:
                indice_max, dmax = le_plus_loin(ligne)
                if dmax <= seuil:
                    return [ligne[0], ligne[n-1]]
                else:
                    return simplifie(extrait(ligne, 0, indice_max), seuil) +  \\
                        simplifie(extrait(ligne, indice_max, n-1), seuil)
        ```        
    """
    )
    }}


    !!! note "Bonus : mise en pratique de l'algorithme de Douglas-Peucker"


    
        Téléchargez d'abord le fichier [coord_france.txt](data/coord_france.txt){. target="_blank"} puis placez-le dans le même dossier que le code Python ci-dessous :


        ```python linenums='1'
        from math import sqrt
        import matplotlib.pyplot as plt

        data = open('coord_france.txt').read().splitlines()
        france = []
        for couple in data:
            cpl = couple.split(',')
            france.append((int(cpl[0]), int(cpl[1])))

        def distance_points(a, b):
            ...

        def distance_point_droite(p, a, b):
            if b[0] == a[0]:
                return abs(p[0]-a[0])
            m = (b[1] - a[1]) / (b[0] - a[0])
            od = a[1] - m*a[0]
            xm = (p[0]*(b[0]-a[0])+(p[1]-od)*(b[1]-a[1])) / (b[0]-a[0] + m*(b[1]-a[1]))
            ym = m*xm + od
            return distance_points(p, (xm, ym))  

        def distance(p, a, b):
            ...
            
        def le_plus_loin(ligne):
            ...


        def extrait(tab, i, j):
            ...

        def simplifie(ligne, seuil):
            ...


        def trace(ligne, seuil):
            new_ligne = simplifie(ligne, seuil)
            nb_segments = len(set(new_ligne))
            x = [p[0] for p in new_ligne]
            y = [p[1] for p in new_ligne]
            plt.plot(x, y, 'b-', linewidth=0.5)
            plt.text(195014, 2865745, 'seuil : ' + str(seuil))
            plt.text(195014, 2864745, 'nb segments : ' + str(nb_segments))
            plt.axis('equal')
            plt.axis('off')
            plt.show()

        trace(france, 0)
        ```




        {{
        correction(False,
        """
        ??? success \"Correction\" 
            ```python linenums='1'
            from math import sqrt
            import matplotlib.pyplot as plt

            data = open('coord_france.txt').read().splitlines()
            france = []
            for couple in data:
                cpl = couple.split(',')
                france.append((int(cpl[0]), int(cpl[1])))

            def distance_points(a, b):
                return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

            def distance_point_droite(p, a, b):
                if b[0] == a[0]:
                    return abs(p[0]-a[0])
                m = (b[1] - a[1]) / (b[0] - a[0])
                od = a[1] - m*a[0]
                xm = (p[0]*(b[0]-a[0])+(p[1]-od)*(b[1]-a[1])) / (b[0]-a[0] + m*(b[1]-a[1]))
                ym = m*xm + od
                return distance_points(p, (xm, ym))  

            def distance(p, a, b):
                if a == b:
                    return distance_points(p, a)
                else:
                    return distance_point_droite(p, a, b)
                
            def le_plus_loin(ligne):
                n = len(ligne)
                deb = ligne[0]
                fin = ligne[n-1]
                dmax = 0
                indice_max = 0
                for idx in range(1, n-1):
                    p = ligne[idx]
                    d = distance(p, deb, fin)
                    if d > dmax:
                        dmax = d
                        indice_max = idx
                return (indice_max, dmax)


            def extrait(tab, i, j):
                ext = []
                for k in range(i, j+1):
                    ext.append(tab[k])
                return ext

            def simplifie(ligne, seuil):
                n = len(ligne)
                if n <= 2:
                    return ligne
                else:
                    indice_max, dmax = le_plus_loin(ligne)
                    if dmax <= seuil:
                        return [ligne[0], ligne[n-1]]
                    else:
                        return simplifie(extrait(ligne, 0, indice_max), seuil) + \
                            simplifie(extrait(ligne, indice_max, n-1), seuil)


            def trace(ligne, seuil):
                new_ligne = simplifie(ligne, seuil)
                nb_segments = len(set(new_ligne))
                x = [p[0] for p in new_ligne]
                y = [p[1] for p in new_ligne]
                plt.plot(x, y, 'b-', linewidth=0.5)
                plt.text(195014, 2865745, 'seuil : ' + str(seuil))
                plt.text(195014, 2864745, 'nb segments : ' + str(nb_segments))
                plt.axis('equal')
                plt.axis('off')
                plt.show()

            trace(france, 0)
            ```    

            Le rendu avec un seuil égal à 0 est celui-ci :

            ![image](data/Figure_1.png){: .center}

            Vous pouvez faire varier le seuil entre 0 et 5000 et observer les modifications.        
        """
        )
        }}


!!! example "{{ exercice() }}"
    Exercice 5 du sujet [Métropole J2 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Metropole_J2.pdf){. target="_blank"}

    {{   
    correction(False,
    """
    ??? success \"Correction Q1.\" 
        ```python
        cellule = Cellule(True, False, True, True)
        ```        
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q2.\" 
        ```python linenums='1' hl_lines='7 9-11'
        class Labyrinthe:
            def __init__(self, hauteur, longueur):
                self.grille = self.construire_grille(hauteur, longueur)

            def construire_grille(self, hauteur, longueur):
                grille = []
                for i in range(hauteur):
                    ligne = []
                    for j in range(longueur):
                        cellule = Cellule(True, True, True, True)
                        ligne.append(cellule)
                    grille.append(ligne)
                return grille
        ```        
    """
    )
    }}




    {{
    correction(False,
    """
    ??? success \"Correction Q3.\" 
        ```python
        cellule2.murs['S'] = False
        ```        
    """
    )
    }}




    {{
    correction(False,
    """
    ??? success \"Correction Q4.\" 
        ```python
        elif c1_lig == c2_lig and c1_col - c2_col == 1:
            cellule1.murs['O'] = False
            cellule2.murs['E'] = False
        ```        
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q5.\" 
        ```python linenums='1' hl_lines='3 6 7'
        def creer_labyrinthe(self, ligne, colonne, haut, long):
            if haut == 1 : # Cas de base
                for k in range(colonne, colonne + long - 1):
                    self.creer_passage(ligne, k, ligne, k + 1)
            elif long == 1: # Cas de base
                for k in range(ligne, ligne + haut - 1):
                    self.creer_passage(k, colonne, k + 1, colonne)
            else: # Appels récursifs
                    # Code non étudié (Ne pas compléter)
        ```        
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q6.\" 
        ![image](data/exo5.png){: .center}  

              
    """
    )
    }}



       
