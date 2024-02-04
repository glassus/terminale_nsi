{{initexo(0)}}

!!! abstract "{{ exercice() }}"

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


    {{
    correction(True,
    """
    ??? success \"Correction Q1.b\" 
        ```python linenums='1'
        def distance_points(a, b):
            return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
        ```        
    """
    )
    }}

    {{
    correction(True,
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


    {{
    correction(True,
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




    {{
    correction(True,
    """
    ??? success \"Correction Q4.\" 
        ```python linenums='1'
        def extrait(tab, i, j):
            ext = []
            for k in range(i, j+1):
                ext.append(tab[k])
            return ext
        ```        
    """
    )
    }}



    {{
    correction(True,
    """
    ??? success \"Correction Q5.\" 
        ```python linenums='1'
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
                        simplifie(extrait(ligne, indice_max+1, n-1), seuil)
        ```        
    """
    )
    }}


    ??? note "Mise en pratique de l'algorithme de Douglas-Peucker"


    
        Téléchargez d'abord le fichier [coord_france.txt](data/coord_france.txt) puis placez-le dans le même dossier que le code Python ci-dessous :


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
                        simplifie(extrait(ligne, indice_max+1, n-1), seuil)


        def trace(ligne, seuil):
            new_ligne = simplifie(ligne, seuil)
            x = [p[0] for p in new_ligne]
            y = [p[1] for p in new_ligne]
            plt.plot(x, y, 'b-', linewidth=0.5)
            plt.text(195014, 2865745, 'seuil : ' + str(seuil))
            plt.axis('equal')
            plt.axis('off')
            plt.show()

        trace(france, 0)
        ```

        Le rendu avec un seuil égal à 0 est celui-ci :

        ![image](data/Figure_1.png){: .center}

        Vous pouvez faire varier le seuil entre 0 et 5000 et observer les modifications.



   