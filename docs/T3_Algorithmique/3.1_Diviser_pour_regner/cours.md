# Diviser pour régner

![image](data/BO.png){: .center}

## 1. Retour sur l'algorithme de dichotomie

Nous avons vu en classe de Première l'algorithme de **dichotomie** (du grec *dikhotomia*, « division en deux parties »).

Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste **triée**.  
Notre fonction renverra donc un booléen.

La recherche *naïve* (élément par élément) est naturellement de complexité linéaire. Nous allons voir que la méthode dichotomique est plus efficace.

### 1.1 Version impérative

!!! note "Dichotomie version impérative :heart:"
    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        i_debut = 0
        i_fin = len(tab) - 1
        while i_debut <= i_fin :
            i_centre = (i_debut + i_fin) // 2     # (1)
            val_centrale = tab[i_centre]          # (2) 
            if val_centrale == val:               # (3) 
                return True
            if val_centrale < val:                # (4) 
                i_debut = i_centre + 1            # (5) 
            else :
                i_fin = i_centre - 1
        return False
    ```

    1. on prend l'indice central
    2. on prend la valeur centrale
    3. si la valeur centrale est la valeur cherchée...
    4. si la valeur centrale est trop petite...
    5. on ne prend pas la valeur centrale qui a déjà été testée

Exemple d'utilisation :

```python
>>> tab = [1, 5, 7, 9, 12, 13]
>>> recherche_dichotomique(tab, 12)
True
>>> recherche_dichotomique(tab, 17)
False
```

À chaque tour de la boucle ```while```, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une **complexité logarithmique** (bien meilleure qu'une complexité linéaire).

### 1.2 Version récursive

#### 1.2.1 Préambule : le slicing
Pour écrire simplement la version récursive de cet algorithme, nous allons avoir besoin de faire du *slicing* (découpage) de listes. Cette manipulation n'est pas au programme de NSI (même si elle est très simple). Attention, elle a un coût algorithmique important, qui peut fausser notre analyse de complexité.

Exemples de slicing :

```python
>>> lst = ['a', 'b', 'c', 'd', 'e']
>>> lst[:2]
['a', 'b']
>>> lst[2:]
['c', 'd', 'e']
```

On comprend que  :

- ```lst[:k]``` va renvoyer la sous-liste composée du premier élément jusqu'à celui d'indice ```k``` **non inclus**.
- ```lst[k:]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au dernier.
- plus généralement, ```lst[k:p]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au ```p```-ième (**non inclus**).

#### 1.2.2 Dichotomie récursive avec slicing

!!! note "Dichotomie version récursive avec slicing :heart:"
    ```python linenums='1'
    def dichotomie_rec(tab, val):
        if len(tab) == 0:
            return False
        i_centre = len(tab) // 2
        if tab[i_centre] == val:
            return True
        if tab[i_centre] < val:
            return dichotomie_rec(tab[i_centre + 1:], val) # (1)
        else:
            return dichotomie_rec(tab[:i_centre], val)  # (2)
    ```

    1. On prend la partie droite de liste, juste après l'indice central.
    2. On prend la partie gauche de liste, juste avant l'indice central.


Exemple d'utilisation :

```python
>>> tab = [1, 5, 7, 9, 12, 13]
>>> dichotomie_rec(tab, 12)
True
>>> dichotomie_rec(tab, 17)
False
```


#### 1.2.3 Dichotomie récursive sans slicing

Il est possible de programmer de manière récursive la recherche dichotomique sans toucher à la liste, et donc en jouant uniquement sur les indices :

!!! note "Dichotomie version récursive sans slicing :heart:"
    ```python linenums='1'
    def dicho_rec_2(tab, val, i=0, j=None): # (1)
        if j is None:                       # (2)
            j = len(tab)-1
        if i > j :
            return False
        m = (i + j) // 2
        if tab[m] < val :
            return dicho_rec_2(tab, val, m + 1, j)
        elif tab[m] > val :
            return dicho_rec_2(tab, val, i, m - 1 )
        else :
            return True
    ```

    1. Pour pouvoir appeler simplement la fonction sans avoir à préciser les indices, on leur donne des paramètres par défaut.
    2. Il est impossible de donner ```j=len(tab)-1``` par défaut (car ```tab``` est aussi un paramètre). On passe donc par une autre valeur (ici ```None```) qu'on va ici intercepter.

Exemple d'utilisation :

```python
>>> tab = [1, 5, 7, 9, 12, 13]
>>> dicho_rec_2(tab, 12)
True
>>> dicho_rec_2(tab, 17)
False
```