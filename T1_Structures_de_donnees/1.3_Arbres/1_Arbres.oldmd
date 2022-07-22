# Arbres

<img src="data/banniere.png" width='70%' />

<img src="data/prog.png" width='70%' />
<img src="data/prog2.png" width='70%' />

## 1. Terminologie

### 1.1 Vocabulaire
Un arbre est une structure hiérarchique de données, composée de nœuds. Si on adopte le vocabulaire des graphes (qui seront vus plus tard dans l'année), un arbre est un graphe non orienté, connexe, sans cycle, et dans lequel un nœud joue le rôle de racine.

![](data/term.png) 


- Chaque **nœud** a exactement un seul **nœud père**, à l'exception du nœud **racine** qui est le seul nœud à ne pas avoir de père. (oui, **la** racine d'une arbre est **en haut**)
<img src="data/real_tree.png" width='30%' />
- Chaque nœud peut avoir un nombre quelconque de **fils**, dont il est le père.
- Les nœuds qui n'ont pas de fils sont appelés les **feuilles** (ou nœuds externes).
- Les nœuds qui ne sont pas des feuilles sont des **nœuds internes**.
- Le nom de chaque nœud est appelé son **étiquette**.

**Exemples :**
dans l'arbre ci-dessus,
- C est la racine, E, Z A et G sont les feuilles.
- K est le père de A et G.
- F est le père de Z.
- C est le père de B et K
- B est le père de E et F.

### 1.2 Exemples d'arbres

#### 1.2.1 La famille royale britannique
<img src="data/windsor.png" width='60%' />

Redessinez de manière plus schématique cet arbre. Pour quelle raison cet arbre a-t-il été modifié par rapport à sa version orginale (voir [ici](https://i.pinimg.com/originals/e8/d1/c7/e8d1c7b2834ce2c368848cf7fc91a057.jpg ) ), qui laissait apparaître les parents de chaque enfant ?

#### 1.2.2 Le DOM d'une page web
DOM : Document Object Model
<img src="data/dom.svg" width='40%' />

#### 1.2.3 L'arborescence d'un disque dur
Les systèmes Unix (MacOS ou GNU/Linux) organisent leur disque dur suivant l'arborescence ci-dessous :
<img src="data/arbo-unix.gif" width='40%' />

#### 1.2.4 Exercice
Quelque part à l'intérieur des dossiers contenus dans l'archive [dossiers.zip](data/dossiers.zip) se trouve un fichier ```tresor.txt```. Quel secret renferme-t-il ?

Attention, cette recherche est à faire uniquement en ligne de commande :
- ```ls``` : pour lister les dossiers et fichiers d'un répertoire
- ```cd Dossier``` : pour se rendre dans le repértoire ```Dossier```
- ```cd ..``` : pour remonter d'un niveau dans l'arborescence
- ```unzip monarchive.zip``` : pour décompresser une archive
- ```tree``` : pour afficher l'arborescence du répertoire courant
- ```sudo apt install monprog``` : pour installer le programme ```monprog``` si celui-ci est manquant.

### 1.3 Caractéristiques d'un arbre

#### 1.3.1 Outils numériques de description

![](data/carac.png)



- la **taille** d'un arbre est son nombre total de nœuds. Ici, elle vaut 8.


- l'**arité** d'un nœud est son nombre de fils. Ici, l'arité de B vaut 2, celle de F vaut 1, celle de Z vaut 0.


- la **profondeur** d'un nœud est le nombre de nœuds de son chemin le plus court vers la racine. 
Ici, la profondeur de G est 3 (G-K-C), la profondeur de B est 2 (B-C), la profondeur de Z est 4 (Z-F-B-C), la profondeur de C est 1.


- la **hauteur** d'un arbre est la profondeur de son nœud le plus profond. 
Ici, la hauteur de l'arbre est 4.
Nous prendrons comme **convention** que :
- si un arbre est réduit à **un seul nœud-racine**, sa hauteur sera **1**.
- si un arbre est **vide**, sa hauteur est **0**.

*Cette convention est celle adoptée dans le sujet 0 publié le 15/12/2020. Attention, dans certains ouvrages, l'arbre vide a pour hauteur -1, et donc l'arbre réduit à un seul nœud a pour hauteur 0, donc notre arbre a une hauteur 3.*

### 1.4 Encore du vocabulaire

#### 1.4.2 Arbres binaires
Un arbre binaire est un arbre dont chaque nœud possède **au plus** deux fils.

L'arbre généalogique de la famille royale britannique n'est pas un arbre binaire. 

L'arbre ci-dessous est lui un arbre binaire.

![](data/carac3.png)

#### 1.4.1 Sous-arbres  d'un arbre binaire

Chaque nœud d'un arbre binaire ne pouvant pas avoir plus de 2 fils, il est possible de séparer le «dessous» de chaque nœud en deux sous-arbres (éventuellement vides) : le **sous-arbre gauche** et le **sous-arbre droit**.

![](data/sousarbres.png)


- Les deux sous-arbres représentés ici sont les sous-arbres du nœud-racine T. 
- Le nœud O admet comme sous-arbre gauche le nœud H et comme sous-arbre droit le nœud N.
- Les feuilles P, H et N ont pour sous-arbre gauche et pour sous-arbre droit l'**arbre vide**.



#### 1.4.3 Cas des arbres binaires complets

On rencontre très souvent des arbres binaires dits **complets** parce qu'aucun des fils gauche ou droit n'est manquant.

![](data/complet.png)


**Taille d'un arbre complet de hauteur $h$ :**
$$1 + 2 + 2^2 + 2^3 + \dots + 2^{h-1} = 2^{h} - 1$$

*preuve* : ceci est la somme $S$ des $h$ premiers termes d'une suite géométrique de raison 2 et de premier terme 1, d'où $S= \frac{1-2^{h}}{1-2} = 2^{h} -1$.


Un arbre complet de hauteur $h$ (en prenant la convention que l'arbre vide a pour hauteur 0) a donc une taille égale à $2^{h}-1$.

**Remarque :** On en déduit une inégalité classique sur l'encadrement de la taille $t$ d'un arbre binaire (non nécessairement complet) de hauteur $h$ :
$$ h \leqslant t \leqslant 2^{h}-1$$

## 2. Parcours d'arbres
Les arbres étant une structure hiérarchique, leur utilisation implique la nécessité d'un **parcours** des valeurs stockées. Par exemple pour toutes les récupérer dans un certain ordre, ou bien pour en chercher une en particulier.  

Il existe plusieurs manières de parcourir un arbre.


### 2.1 Parcours en largeur d'abord (BFS)
*BFS : Breadth First Search*

Le parcours en largeur d'abord est un parcours étage par étage (de haut en bas) et de gauche à droite.

![](data/BFS.png)

L'ordre des lettres parcourues est donc T-Y-O-P-H-N.

Les trois parcours que nous allons voir maintenant sont des parcours en **profondeur d'abord**, ou **DPS** (*Depth First Search*). Ce qui signifie qu'un des deux sous-arbres sera totalement parcouru avant que l'exploration du deuxième ne commence. 

### 2.2 Parcours préfixe
Le parcours **préfixe** est un parcours **en profondeur d'abord**. 

**Méthode du parcours préfixe :** (parfois aussi appelé *préordre*)
- Chaque nœud est visité avant que ses fils le soient.
- On part de la racine, puis on visite son fils gauche (et éventuellement le fils gauche de celui-ci, etc.) avant de remonter et de redescendre vers le fils droit.

![](data/prefixe.png)

L'ordre des lettres parcourues est donc T-Y-P-O-H-N.

### 2.3 Parcours infixe
Le parcours **infixe** est aussi un parcours en profondeur d'abord.

**Méthode du parcours infixe :** (parfois aussi appelé *en ordre*)
- Chaque nœud est visité **après son fils gauche mais avant son fils droit**.
- On part donc de la feuille la plus à gauche et on remonte par vagues sucessives. Un nœud ne peut pas être visité si son fils gauche ne l'a pas été.

![](data/infixe.png)

L'ordre des lettres parcourues est donc P-Y-T-H-O-N.

### 2.4 Parcours postfixe
Le parcours **postfixe** est aussi un parcours en profondeur d'abord.

**Méthode du parcours postfixe :** (parfois aussi appelé *post ordre*)
- Chaque nœud est visité **après ses fils le soient**.
- On part donc de la feuille la plus à gauche, et on ne remonte à un nœud père que si ses fils ont tous été visités. 

![](data/postfixe.png)

L'ordre des lettres parcourues est donc P-Y-H-N-O-T.

### 2.5 Comment ne pas se mélanger entre le pré / in / post fixe ?
- *pré* veut dire *avant*
- *in* veut dire *au milieu*
- *post* veut dire *après*

Ces trois mots-clés parlent de la place du **père** par rapport à ses fils. 
Ensuite, il faut toujours se souvenir qu'on traite le fils gauche avant le fils droit.

- préfixe : le père doit être le premier par rapport à ses fils.
- infixe : le père doit être entre son fils gauche (traité en premier) et son fils droit.
- postfixe : le père ne doit être traité que quand ses deux fils (gauche d'abord, droite ensuite) l'ont été.

Un parcours préfixe commencera toujours par la racine, alors qu'un parcours postfixe finira toujours par la racine. Dans un parcours infixe, la racine sera «au milieu» (pas nécessairement parfaitement).

### 2.6 Exercice 1

![](data/exo_parcours.png)

Donner le rendu de chaque parcours :
1. Parcours en largeur 
2. Parcours préfixe
3. Parcours infixe
4. Parcours postfixe

[Correction](https://gist.github.com/glassus/031901b09dbb9d780247beb5db69eda2)


### 2.7 Exercice 2

![](data/exo_2.png)

Donner le rendu de chaque parcours :
1. Parcours en largeur 
2. Parcours préfixe
3. Parcours infixe
4. Parcours postfixe

[Correction](https://gist.github.com/glassus/05aeb20012b01bbaa170aa78c6959a0e)


## 3. Implémentations d'un arbre binaire
### 3.1 En utilisant la Programmation Orientée Objet
Le but est d'obtenir l'interface ci-dessous.

Il est à remarquer que ce que nous allons appeler «Arbre» est en fait un nœud et ses deux fils gauche et droit.


```python
a = Arbre(4) # pour créer l'arbre dont le nœud a pour valeur 4,
             # et dont les sous-arbres gauche et droit sont None
```


```python
a.set_left(Arbre(3)) # pour donner la valeur 3 au nœud du sous-arbre gauche de a
```


```python
a.set_right(Arbre(1)) # pour donner la valeur 1 au nœud du sous-arbre droit de a
```


```python
a.get_right() # pour accéder au sous-arbre droit de a
```


```python
a.get_left() # pour accéder au sous-arbre gauche de a
```


```python
a.get_data() # pour accéder à la valeur du nœud de l'arbre a
```

**Exercice :** Dessinez l'arbre créé par les instructions suivantes :


```python
a = Arbre(4)
a.set_left(Arbre(3))
a.set_right(Arbre(1))
a.get_right().set_left(Arbre(2))
a.get_right().set_right(Arbre(7))
a.get_left().set_left(Arbre(6))
a.get_right().get_right().set_left(Arbre(9))
```

[correction](data/exo_imp.png)

**🟊 Implémentation 🟊**

⯈ **Principe** : nous allons créer une classe ```Arbre```, qui contiendra 3 attributs : 
- ```data``` : la valeur du nœud (de type ```Int```)
- ```left``` : le sous-arbre gauche (de type ```Arbre```)
- ```right``` : le sous-arbre droit (de type ```Arbre```).

Par défaut, les attributs ```left ``` et ```right``` seront à ```None```, qui représentera l'arbre vide (ce qui n'est pas très rigoureux, car ```None``` n'est pas de type ```Arbre```...).

⯈ **Parti-pris** : afin de respecter le paradigme de la Programmation Orientée Objet, nous allons (pour une fois) jouer totalement le jeu de l'**encapsulation** en nous refusant d'accéder directement aux attributs.

Nous allons donc construire des méthodes permettant d'accéder à ces attributs (avec des **getters**, ou **accesseurs** en français) ou de les modifier (avec des **setters**, ou **mutateurs** en français) .

Dans certains langage (Java, C#...) , l'encapsulation est vivement encouragée : il est possible de limiter concrètement la visibilité des attributs (par les mots-clés ```private``` ou ```protected```).



```python
class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, sousarbre):
        self.left = sousarbre

    def set_right(self, sousarbre):
        self.right = sousarbre  

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data
```

L'implémentation précédente permet d'utiliser les instructions de l'exercice précédent et de vérifier que l'arbre a bien été créé.


```python
a = Arbre(4)
a.set_left(Arbre(3))
a.set_right(Arbre(1))
a.get_right().set_left(Arbre(2))
a.get_right().set_right(Arbre(7))
a.get_left().set_left(Arbre(6))
a.get_right().get_right().set_left(Arbre(9))
```


```python
a
```




    <__main__.Arbre at 0x7f0100361f40>




```python
a.get_right().get_left().get_data()
```




    2



### 3.2 Implémentation à partir de tuples imbriqués

Considérons qu'un arbre peut se représenter par le tuple ```(valeur, sous-arbre gauche, sous-arbre droit)```.

L'arbre ci-dessous :
![](data/imp_tuple.png)
peut alors être représenté par le tuple :


```python
a = (2, (8, (6,(),()), (9,(),())), (1, (7, (),()), ()))
```

Le sous-arbre gauche est alors ```a[1]``` et le sous-arbre droit est ```a[2]```.


```python
a[1]
```




    (8, (6, (), ()), (9, (), ()))




```python
a[2]
```




    (1, (7, (), ()), ())



**Exercice :** écrire le tuple représentant l'arbre ci-dessous.

![](data/carac3.png)

[correction](https://gist.github.com/glassus/4056ad7c0a0409126ccce517c6afeb4f)


```python

```

### 3.3 Implémentation à partir d'une «simple» liste
De manière plus surprenante, il existe une méthode pour implémenter un arbre binaire (qui est une structure hiérarchique) avec une liste (qui est une structure linéaire). 
Ceci peut se faire par le biais d'une astuce sur les indices :

**Les fils du nœud d'indice i sont placés aux indice 2i+1 et 2i+2**.

Cette méthode est connue sous le nom de «méthode d'Eytzinger», et utilisée notamment en [généalogie](https://fr.wikipedia.org/wiki/Num%C3%A9rotation_de_Sosa-Stradonitz) pour numéroter facilement les individus d'un arbre généalogique.



**Exemple :**

![](data/eytzinger.png)


Pour comprendre facilement la numérotation, il suffit de s'imaginer l'arbre complet (en rajoutant les fils vides) et de faire une numérotation en largeur, niveau par niveau :

![](data/eytzinger2.png)

**Exercice :** Si on note Δ le sous-arbre vide, dessiner l'arbre représenté par la liste :


```python
a = [3,4,Δ,7,5,Δ,Δ]
```

[correction](data/corrtuple.png)

**Remarque :** parfois (comme dans le sujet 0...) la racine de l'arbre est placée à l'indice 1. Dans ce cas, les fils du nœud d'indice i sont placés aux indice 2i et 2i+1.

## 4. Utilisation de l'implémentation : parcours, taille...

Dans toute la suite, sauf mention contraire, on utilisera l'implémentation en Programmation Orientée Objet.
Nous allons créer des fonctions renvoyant les différents parcours d'un arbre, ou encore sa taille, sa hauteur, son nombre de feuilles... Toutes ses fonctions exploiteront la structure **récursive** d'un arbre.


**Rappel de l'implémentation :**


```python
class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, sousarbre):
        self.left = sousarbre

    def set_right(self, sousarbre):
        self.right = sousarbre  

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data
```

### 4.1 Parcours préfixe, infixe, postfixe

#### 4.1.1 Parcours préfixe


```python
def prefixe(arbre):
    if arbre is None :
        return 0
    print(arbre.data, end = '-')
    prefixe(arbre.left)
    prefixe(arbre.right)

```

Exemple avec l'arbre 
![](data/exo_2.png)


```python
a = Arbre(9)
a.set_left(Arbre(8))
a.set_right(Arbre(7))
a.get_left().set_left(Arbre(6))
a.get_left().set_right(Arbre(2))
a.get_right().set_right(Arbre(5))
a.get_left().get_right().set_left(Arbre(1))
a.get_right().get_right().set_left(Arbre(4))
a.get_right().get_right().set_right(Arbre(3))
```


```python
prefixe(a)
```

    9-8-6-2-1-7-5-4-3-

#### 4.1.2 Parcours infixe


```python
def infixe(arbre):
    if arbre is None :
        return 0
    infixe(arbre.left)
    print(arbre.data, end = '-')
    infixe(arbre.right)
```


```python
infixe(a)
```

    6-8-1-2-9-7-4-5-3-

#### 4.1.3 Parcours postfixe


```python
def postfixe(arbre):
    if arbre is None :
        return 0
    postfixe(arbre.left)
    postfixe(arbre.right)
    print(arbre.data, end = '-')
```


```python
postfixe(a)
```

    6-1-2-8-4-3-5-7-9-

### 4.2 Calcul de la taille d'un arbre
Rappel :la taille d'un arbre est le nombre de ses nœuds.


```python
def taille(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + taille(arbre.get_left()) + taille(arbre.get_right())
```


```python
taille(a)
```




    9



### 4.3 Calcul de la hauteur d'un arbre
Rappel : on prendra comme convention que l'arbre vide a pour hauteur 0.


```python
def hauteur(arbre):
    if arbre is None:
        return 0
    else :
        return 1 + max(hauteur(arbre.get_left()),hauteur(arbre.get_right()))
```


```python
hauteur(a)
```




    4



### 4.4 Calcul du nombre de feuilles d'un arbre
Rappel : une feuille est un nœud d'arité 0, autrement dit sans fils gauche ni fils droit.


```python
def nbfeuilles(arbre):
    if arbre is None:
        return 0
    if (arbre.get_left() is None) and (arbre.get_right() is None):
        return 1
    else :
        return nbfeuilles(arbre.get_left()) +  nbfeuilles(arbre.get_right())
```


```python
nbfeuilles(a)
```




    4



### 4.5 Rechercher une valeur dans un arbre
On renverra ```True``` ou ```False``` en fonction de la présence ou non de la valeur dans l'arbre.


```python
def recherche(arbre, valeur):
    if arbre is None:
        return False
    if arbre.get_data() ==  valeur:
        return True
    else :
        return recherche(arbre.get_left(), valeur) or recherche(arbre.get_right(), valeur)
```


```python
recherche(a, 2)
```




    True




```python
recherche(a, 45)
```




    False



### 4.6 Parcours en largeur
Le parcours en largeur (BFS) est le plus simple à faire visuellement : mais il est plus difficile à coder que les parcours préfixe, infixe, postfixe.  
Il est nécessaire d'utiliser une **file**  :
- On place l'arbre dans la file.
- Tant que la file n'est pas vide, on procède comme suit :
    - On défile, donc on récupère l'arbre situé en haut de la file.  
    - Si cet arbre n'est pas vide :
        - On garde son étiquette.
        - On enfile son sous-arbre gauche, puis son sous-arbre droit.

![](data/parcoursBFS.png)

On importera l'objet ```Queue()``` du module ```queue``` de Python, qui permet de  :
- créer une file vide avec ```file = Queue()```
- défiler un élément par ```file.get()```
- enfiler l'élément ```a``` par ```file.put(a)```
- savoir si la file est vide par le booléen ```file.empty()```


```python
# arbre-test
# ne pas oublier de remonter plus haut dans le document pour relancer la classe Arbre
a = Arbre(8)
a.set_left(Arbre(4))
a.set_right(Arbre(5))
a.get_left().set_left(Arbre(2))
a.get_left().set_right(Arbre(1))
a.get_right().set_right(Arbre(3))
```


```python
from queue import Queue

def BFS(arbre):        
    file = Queue()
    file.put(arbre)
    sol = []
    while file.empty() is False :
        a = file.get()
        if a is not None :
            sol.append(a.get_data())
            file.put(a.get_left())
            file.put(a.get_right())
    return sol
```


```python
BFS(a)
```




    [8, 4, 5, 2, 1, 3]



## 5. Arbres binaires de recherche (ABR)
Un **arbre binaire de recherche** est un arbre binaire dont les valeurs des nœuds (valeurs qu'on appelle étiquettes, ou clés) vérifient la propriété suivante :
- l'étiquette d'un nœud est **supérieure ou égale** à celle de **chaque** nœud de son **sous-arbre gauche**.
- l'étiquette d'un nœud est **strictement inférieure** à celle du **chaque** nœud de son **sous-arbre droit**.

![](data/exABR.png)

À noter que l'arbre 3 (qui est bien un ABR) est appelé **arbre filiforme**. 

L'arbre 5 n'est pas un ABR à cause de la feuille 9, qui fait partie du sous-arbre gauche de 3 sans lui être inférieure.

**Remarque :** on pourrait aussi définir un ABR comme un arbre dont le parcours infixe est une suite croissante.

### 5.1 Déterminer si un arbre est un ABR

Employer une méthode récursive imposerait de garder en mémoire dans l'exploration des sous-arbres la valeur maximale ou minimale. Nous allons plutôt utiliser la remarque précédente, et nous servir du parcours infixe.

Méthode : récupérer le parcours infixe dans une liste, et faire un test sur cette liste.


```python
def est_ABR(arbre, p):
    '''renvoie un booléen indiquant si arbre est un ABR'''
    # p est la liste qui contiendra le parcours. la fonction est à appeler par est_ABR(a, [])
    if arbre is None :
        return 0
    est_ABR(arbre.left, p)
    p.append(arbre.data)
    est_ABR(arbre.right, p)
    return p == sorted(p) # on regarde si le parcours est égal au parcours trié (merci TomFox)

```


```python
# arbres-tests 

#arbre n°4
a = Arbre(5)
a.set_left(Arbre(2))
a.set_right(Arbre(7))
a.get_left().set_left(Arbre(0))
a.get_left().set_right(Arbre(3))
a.get_right().set_left(Arbre(6))
a.get_right().set_right(Arbre(8))

#arbre n°5
b = Arbre(3)
b.set_left(Arbre(2))
b.set_right(Arbre(5))
b.get_left().set_left(Arbre(1))
b.get_left().set_right(Arbre(9))
b.get_right().set_left(Arbre(4))
b.get_right().set_right(Arbre(6))


```


```python
est_ABR(a, [])
```




    True




```python
est_ABR(b, [])
```




    False



### 5.2 Rechercher une clé dans un ABR

Un arbre binaire de taille $n$ contient $n$ clés (pas forcément différentes). Pour savoir si une valeur particulière fait partie des clés, on peut parcourir tous les nœuds de l'arbre, jusqu'à trouver (ou pas) cette valeur dans l'arbre. Dans le pire des cas, il faut donc faire $n$ comparaisons.

Mais si l'arbre est un ABR, le fait que les valeurs soient «rangées» va considérablement améliorer la vitesse de recherche de cette clé, puisque la moitié de l'arbre restant sera écartée après chaque comparaison.


```python
def contient_valeur(arbre, valeur):
    if arbre is None :
        return False
    if arbre.get_data() == valeur :
        return True
    if valeur < arbre.get_data() :
        return contient_valeur(arbre.get_left(), valeur)
    else:
        return contient_valeur(arbre.get_right(), valeur)

```

**Exemple** 

L'arbre ```a``` contient la valeur 8, mais l'arbre ```b``` ne la contient pas :



```python
contient_valeur(a,8)
```




    True




```python
contient_valeur(b,8)
```




    False



### 5.3  Coût de la recherche dans un ABR équilibré
![](data/rechercheABR.png)

Imaginons un arbre équilibré de taille $n$. Combien d'étapes faudra-t-il, dans le pire des cas, pour trouver (ou pas) une clé particulière dans cet arbre ?

Après chaque nœud, le nombre de nœuds restant à explorer est divisé par 2. On retrouve là le principe de recherche dichotomique, vu en classe de Première (voir [ici](https://github.com/glassus/nsi/blob/master/Premiere/Theme05_Algorithmique/05_Dichotomie.ipynb)).

S'il faut parcourir tous les étages de l'arbre avant de trouver (ou pas) la clé recherchée, le nombre de nœuds parcourus est donc égal à la hauteur $h$ de l'arbre.

Pour un arbre complet, cette hauteur vérifie la relation $2^h -1= n$. et donc $2^h = n+1$.

$h$ est donc le «nombre de puissance de 2» que l'on peut mettre dans $n+1$. Cette notion s'appelle le logarithme de base 2 et se note $\log_2$.

Par exemple, $\log_2(64)=6$ car $2^6=64$.

Le nombre maximal de nœuds à parcourir pour rechercher une clé dans un ABR équilibré de taille $n$ est donc de l'ordre de $\log_2(n)$, ce qui est très performant !

Pour arbre contenant 1000 valeurs, 10 étapes suffisent.

Cette **complexité logarithmique** est un atout essentiel de la structure d'arbre binaire de recherche.

### 5.4  Insertion dans un ABR
L'insertion d'une clé va se faire au niveau d'une feuille, donc au bas de l'arbre. Dans la version récursive de l'algorithme d'insertion, que nous allons implémenter, il n'est pourtant pas nécessaire de descendre manuellement dans l'arbre jusqu'au bon endroit : il suffit de distinguer dans lequel des deux sous-arbres gauche et droit doit se trouver la future clé, et d'appeler récursivement la fonction d'insertion dans le sous-arbre en question.

**Algorithme :**
- Si l'arbre est vide, on renvoie un nouvel objet Arbre contenant la clé.
- Sinon, on compare la clé à la valeur du nœud sur lequel on est positionné :
    - Si la clé est inférieure à cette valeur, on va modifier le sous-arbre gauche en le faisant pointer vers ce même sous-arbre une fois que la clé y aura été injecté, par un appel récursif.
    - Si la clé est supérieure, on fait la même chose avec l'arbre de droite.
    - on renvoie le nouvel arbre ainsi créé.


```python
def insertion(arbre, valeur):
    if arbre is None :
        return Arbre(valeur)
    else :
        v = arbre.get_data()
        if valeur <= v :
            arbre.set_left(insertion(arbre.get_left(), valeur))
        else:
            arbre.set_right(insertion(arbre.get_right(), valeur))
        return arbre
```

**Exemple :** Nous allons insérer la valeur 4 dans l'arbre ```a``` et vérifier par un parcours infixe (avant et après l'insertion) que la valeur 4 a bien été insérée au bon endroit.

![](data/insertionABR.png)


```python
a = Arbre(5)
a.set_left(Arbre(2))
a.set_right(Arbre(7))
a.get_left().set_left(Arbre(0))
a.get_left().set_right(Arbre(3))
a.get_right().set_left(Arbre(6))
a.get_right().set_right(Arbre(8))
```


```python
infixe(a)
```

    0-2-3-5-6-7-8-


```python
insertion(a,4)
```




    <__main__.Arbre at 0x7f46f0507e80>




```python
infixe(a)
```

    0-2-3-4-5-6-7-8-

La valeur 4 a donc bien été insérée au bon endroit.



---
## Bibliographie
- Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.



---

![](../../../ccbysa.png "image") G.Lassus, Lycée François Mauriac --  Bordeaux  

