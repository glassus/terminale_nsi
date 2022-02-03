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

??? aide "Visualisation grâce à PythonTutor:"
    <iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20dichotomie_rec%28tab,%20val%29%3A%0A%20%20%20%20if%20len%28tab%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20i_centre%20%3D%20len%28tab%29%20//%202%0A%20%20%20%20if%20tab%5Bi_centre%5D%20%3D%3D%20val%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20if%20tab%5Bi_centre%5D%20%3C%20val%3A%0A%20%20%20%20%20%20%20%20return%20dichotomie_rec%28tab%5Bi_centre%20%2B%201%3A%5D,%20val%29%20%23%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20dichotomie_rec%28tab%5B%3Ai_centre%5D,%20val%29%20%20%23%20%0A%0Atab%20%3D%20%5B1,%205,%207,%209,%2012,%2013%5D%0Adichotomie_rec%28tab,%206%29%0Adichotomie_rec%28tab,%2012%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

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

## 2. Diviser pour régner

Les algorithmes de dichotomie présentés ci-dessous ont tous en commun de diviser par deux la taille des données de travail à chaque étape. Cette méthode de résolution d'un problème est connue sous le nom de *diviser pour régner*, ou *divide and conquer* en anglais.  

Une définition pourrait être :

!!! abstract "Définition :heart:"
    Un problème peut se résoudre en employant le paradigme *diviser pour régner* lorsque :  
    - il est possible de décomposer ce problème en sous-problèmes **indépendants**.  
    - la taille de ces sous-problèmes est une **fraction** du problème initial


**Remarques :**

- Les sous-problèmes peuvent nécessiter d'être ensuite recombinés entre eux (voir plus loin le tri fusion).
- Considérons de l'écriture récursive de la fonction ```factorielle``` ci-dessous :
```python
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
``` 
On ne peut pas parler ici de *diviser pour régner* car la taille des données à traiter est passée de *n* à *n-1*. C'est bien une diminution (qui fait que l'algorithme fonctionne) mais il n'y a pas de **division** de la taille des données.  
C'est cette division (par 2 dans le cas de la dichotomie) qui donne son efficacité à ce paradigme.

- Le paradigme *diviser pour régner* va naturellement amener à rédiger des programmes récursifs.


## 3. L'exponentiation rapide
On appelle *exponentiation* le fait de mettre en puissance un nombre. On va donc coder, de deux manières différentes, la puissance d'un nombre.

### 3.1 Algorithme classique

!!! note "Exponentiation classique :heart:"
    ```python linenums='1'
    def puissance(a, n):
        if n == 0:
            return 1
        else:
            return a * puissance(a, n-1)
    ```

### 3.2 Algorithme utilisant *diviser pour régner*

Nous allons nous appuyer sur la remarque mathématique suivante :  
Pour tout nombre $a$, 

- si $n$ est pair, $a^n = (a^2)^{\frac{n}{2}}$

- si $n$ est impair, $a^n = a \times a^{n-1} = a \times (a^2)^{\frac{n-1}{2}}$

Ainsi, dans le cas où $n$ est pair, il suffit d'élever $a$ au carré (une seule opération) pour que l'exposant diminue de **moitié**. On peut donc programmer la fonction ```puissance```  en utilisant le paradigme *diviser pour régner* : 


!!! note "Exponentiation rapide :heart:"
    ```python linenums='1'
    def puissance_mod(a, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return puissance_mod(a*a, n//2)
        else:
            return a * puissance_mod(a*a, (n-1)//2)
    ```


### 3.3 Comparaison de la vitesse d'exécution des deux algorithmes

![image](data/puiss.png){: .center}

!!! example "Exercice"
    === "Énoncé"
        Recréer le graphique ci-dessus, qui compare les temps d'exécution des deux fonctions ```puissance``` et ```puissance_mod```.

        **Aide pour Matplotlib :** le code ci-dessous

        ```python linenums='1'
        import matplotlib.pyplot as plt

        def carre(x):
            return x*x

        x = list(range(10))
        y = [carre(k) for k in x]
        plt.plot(x, y)
        plt.show()
        ```

        donne le graphique suivant :

        ![image](data/carre.png){: .center}
        