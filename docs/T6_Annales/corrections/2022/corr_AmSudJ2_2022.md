# Correction du sujet 22-NSIJ2AS1 / Amérique du Sud J2 2022

:arrow_right: [Sujet](../../data/2022/2022_Amerique_Sud_J2.pdf){. target="_blank"}

## Exercice 1

??? tip "Correction Q1"
    ```python linenums='1' hl_lines='6 7 8'
    def plus_proche_voisin(t, cible) :
        dmin = distance(t[0], cible)
        idx_ppv = 0
        n = len(t)
        for idx in range(1, n) :
            if distance(t[idx], cible) < dmin:
                dmin = distance(t[idx], cible)
                idx_ppv = idx
        return idx_ppv
    ```

??? tip "Correction Q2"
    La complexité est linéaire, car le nombre d'opérations est proportionnel à la taille du tableau ```t```.

??? tip "Correction Q3.a"
    Il suffit d'insérer la ligne ```dist = distance(obj, cible)``` en dessous de la boucle ```for``` et d'utiliser cette variable ```dist``` partout à la place de ```distance(obj, cible)```.

??? tip "Correction Q3.b"
    La complexité (même répétée) d'une opération d'insertion d'un seul élément à sa bonne place dans une liste est moindre que celle d'un tri global. (NDLR : pas sûr)

??? tip "Correction Q3.c"
    ```python linenums='1'
    def insertion(kppv, idx, d):
        i = 0
        while d < kppv[i][1] and i < len(kppv):
            i += 1
        kppv.insert(i, (idx, d)) 
    ```


## Exercice 2

### Partie A

??? tip "Correction Q1"
    ```ifconfig``` 

??? tip "Correction Q2"
    ```DHCP``` (NDLR : question hors-programme)

??? tip "Correction Q3"
    ```192.168.1.1``` 

??? tip "Correction Q4"
    C’est possible et cette adresse serait celle de la box vers Internet. 

??? tip "Correction Q5"
    Oui, car les adresses 192.168.x.x ne sont pas routées sur Internet. 

### Partie B

??? tip "Correction Q1"
    $C = \dfrac{10^9}{50 \times 10^6}=\dfrac{1000}{50}=20$

??? tip "Correction Q2.a."
    ![image](data/ASJ2_exo2.png){: .center}

??? tip "Correction Q2.b."
    Suivant le protocole OSPF, il faut minimiser le coût total. Il faut pour cela suivre le chemin R1-R3-R6-R7-R4-R5-R8, pour un coût total de 80.

??? tip "Correction Q3.c."
    Pour que le protocole OSPF fasse passer par la liaison R1-R4, il faut que celle-ci ait un coût inférieur à la liaison actuelle R1-R3-R6-R7-R4, qui a un coût de 40.  
    Il faut donc que le coût R1-R4 soit inférieur à 40, ce qui sera le cas pour une bande passante supérieure à 25 Mb/s (car $\dfrac{10^9}{25 \times 10^6}=40$)
    
    
## Exercice 3

??? tip "Correction Q1"
    ```sql
    UPDATE ModeleVelo
    SET Stock = 0
    WHERE nomModele = "Bovelo";
    ```

??? tip "Correction Q2"
    Il faut effectuer d'abord la requête 4 (qui déclare le nouveau fabricant, qui aura pour ```idFabricant``` 3127), puis la requête 2 (où on peut retrouver l'id 3127).

??? tip "Correction Q3.a."
    ```sql
    SELECT nomModele, idFabricant
    FROM ModeleVelo
    WHERE Stock = 0;
    ```

??? tip "Correction Q3.b."
    ```sql
    SELECT COUNT(numeroCommande)
    FROM Commande
    WHERE date >= '2022-01-01';
    ```

??? tip "Correction Q3.c."
    ```sql
    SELECT Fabricant.nom
    FROM Fabricant
    JOIN ModeleVelo ON Fabricant.idFabricant = ModeleVelo.idFabricant
    WHERE ModeleVelo.Stock > 0
    ```

??? tip "Correction Q4."
    Cette requête permet d'obtenir le nom de tous les clients ayant acheté le modèle de vélo "Bovelo". Si certains l'ont acheté en plusieurs exemplaires, leur nom n'apparaitra qu'une seule fois.

## Exercice 4

??? tip "Correction Q1.a."
    ```python
    from math import sqrt
    ```

??? tip "Correction Q1.b."
    ```python linenums='1'
    def distance_points(a, b):
        return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
    ```
    
??? tip "Correction Q2."
    ```python linenums='1'
    def distance(p, a, b):
        if a == b:
            return distance_points(p, a)
        else:
            return distance_point_droite(p, a, b)
    ```

??? tip "Correction Q3."
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

??? tip "Correction Q4."
    ```python linenums='1'
    def extrait(tab, i, j):
        ext = []
        for k in range(i, j+1):
            ext.append(tab[k])
        return ext
    ```

## Mise en pratique de l'algorithme de Douglas-Peucker (exercice 4)

```python linenums='1'
from math import sqrt
import matplotlib.pyplot as plt

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


france = [(8.74, 14.18),(8.12, 13.96),(8.08, 13.14),(7.62, 12.8),
         (7.04, 12.5),(6.84, 12.24),(6.52, 12.04),(5.86, 12.14),
         (5.74, 12.56),(5.26, 12.58),(5.34, 12.12),(5.48, 11.64),
         (5.54, 11.28),(5.18, 11.3),(4.76, 11.26),(4.46, 11.14),
         (4.24, 11.62),(3.86, 11.58),(3.50, 11.48),(2.80, 11.3),
         (2.90, 11.0), (3.18, 10.78),(2.68, 10.68),(3.04, 10.5),
         (3.60, 10.3),(4.06, 10.02),(4.44, 9.92),(4.62, 9.62),
         (4.98, 9.32),(4.92, 8.94),(5.04, 8.52),(5.52, 8.38),
         (5.66, 7.98),(5.58, 7.64),(5.96, 7.22),(5.66, 7.26),
         (5.52, 6.46),(5.46, 5.72),(5.24, 5.04),(5.00, 4.74),
         (5.34, 4.52),(5.72, 4.20),(6.24, 3.98),(6.86, 3.86),
         (7.18, 3.80),(7.34, 4.04),(7.64, 3.82),(8.04, 3.74),
         (8.28, 3.42),(8.76, 3.46),(9.04, 3.50),(9.42, 3.52),
         (9.32, 4.08),(9.78, 4.58),(10.3, 4.86),(10.66, 4.76),
         (11.18, 4.64),(11.56, 4.48),(12.22, 4.42),(12.68, 4.54),
         (12.98, 5.08),(13.42, 5.64),(12.86, 5.84),(12.68, 6.32),
         (12.8, 6.66),(12.34, 6.86),(12.86, 7.22),(12.58, 7.68),
         (12.68, 8.00),(12.48, 8.38),(12.04, 8.52),(11.84, 8.12),
         (11.9, 8.82), (12.44, 9.46),(12.98, 9.92),(13.04, 10.5),
         (13.08, 11.22),(13.46, 11.76),(12.78, 11.86),(12.26, 11.96),
         (11.8, 12.34),(11.14, 12.34),(10.72, 12.72),(10.62, 13.16),
         (10.3, 12.78),(9.98, 12.9),(10.04, 13.34),(9.64, 13.4),
         (9.34, 13.54),(9.34, 13.92),(8.92, 13.82),(8.74, 14.18)]

def trace(ligne, seuil):
    new_ligne = simplifie(ligne, seuil)
    x = [p[0] for p in new_ligne]
    y = [p[1] for p in new_ligne]
    plt.plot(x, y, 'r-')
    plt.text(2, 14, 'seuil : ' + str(seuil))
    plt.axis('equal')
    plt.show()

trace(france, 0)

```

![image](data/Figure_1.png){: .center}
![image](data/Figure_2.png){: .center}
![image](data/Figure_3.png){: .center}
![image](data/Figure_4.png){: .center}
