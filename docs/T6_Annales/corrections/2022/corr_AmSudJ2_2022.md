# Sujet 22-NSIJ2AS1 Amérique du Sud J2 2022

[Sujet](../../data/2022/2022_Amerique_Sud_J2.pdf){. target="_blank"}

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