## Exercice 1
Écrire une fonction récursive ```puissance(x,n)``` qui calcule le nombre $x^n$.


```python
def puissance(x,n):
  if n == 0 :
    return 1
  else :
    return x*puissance(x,n-1)
```


```python
puissance(2,10)
```




    1024



## Exercice 2
Écrire une fonction récursive ```boucle(i,k)``` qui affiche les entiers entre ```i``` et ```k```. Par exemple, ```boucle(2,5)``` doit afficher ```2 3 4 5```


```python
def boucle(i,k):
  if i == k :
    print(i)
  else :
    print(i)
    boucle(i+1,k)
```


```python
boucle(2,5)
```

    2
    3
    4
    5



```python

```

## Exercice 3
On rappelle que le PGCD (plus grand diviseur commun de deux nombres) vérifie la propriété suivante : si la division euclidienne de $a$ par $b$ s'écrit $a = b \times q + r$, alors $pgcd(a,b)=pgcd(b,r)$. 

Cette propriété est à la base de l'algorithme d'Euclide

Exemple : $pgcd(24,18)=pgcd(18,6)=pgcd(6,0)$, donc $pgcd(24,18)=6$

Écrire un algorithme récursif ```pgcd(a,b)```.


```python
def pgcd(a,b):
  if b == 0 :
    return a
  else :
    return pgcd(b,a%b)

def pgcd2(a,b):
  return a if b == 0 else pgcd2(b,a%b)


print(pgcd(18,12))
print(pgcd2(18,12))
```

    6
    6


## Exercice 4
La conjecture de Syracuse (ou de Collatz) postule ceci :  

*Prenons un nombre $n$ : si $n$ est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber sur le nombre 1.*

Proposer un programme récursif ```syracuse(n)``` écrivant tous les termes de la suite de Syracuse, s'arrêtant (on l'espère) à la valeur 1.


```python
def syracuse(n):
  print(n)
  if n == 1 :
    return None
  else :
    if n % 2 == 0 :
      return syracuse(n//2)
    else :
      return syracuse(3*n+1)
```


```python
syracuse(14)
```

    14
    7
    22
    11
    34
    17
    52
    26
    13
    40
    20
    10
    5
    16
    8
    4
    2
    1


## Exercice 5
Reproduire le dessin suivant, à l'aide du module ```turtle```.  

```turtle``` est un hommage au langage LOGO inventé par [Seymour Papert](https://fr.wikipedia.org/wiki/Seymour_Papert) au MIT à la fin des années 60.

![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/carres_turtle.png?raw=1)


```python
from turtle import *


def carre(c):
    for k in range(4):
        forward(c)
        right(90)

def base(c):
    carre(c)
    forward(c/2)
    right(45)

def trace(c):
    if c < 5 :
        return None
    else :
        base(c)
        return trace(c/(2**0.5))
    
trace(200)
```

## Exercice 6
Proposer une nouvelle fonction récursive ```puissance(x,n)``` qui calcule le nombre $x^n$. Pour optimiser la fonction déjà construite à l'exercice 1, utiliser le fait que :
- si $n$ est pair, $a^n=(a \times a)^{n/2}$
- sinon $a^n=a \times (a \times a)^{(n-1)/2}$


```python
def puissance(x,n):
  if n == 0 :
    return 1
  else :
    if n % 2 == 0:
      return puissance(x*x,n//2)
    else :
      return x*puissance(x*x,(n-1)//2)
```


```python
puissance(10,3)
```




    1000




```python
puissance(10,6)
```




    1000000



## Exercice 7
Écrire un algorithme récursif ```recherche(lst,m)``` qui recherche la présence de la valeur ```m``` dans une liste triée ```lst```. Cette fonction doit renvoyer un booléen.


```python
lst=[5,6,9,12,17]
```


```python
lst[:3]
```

    [5, 6, 9]



```python
lst[3:]
```




    [12, 17]




```python
def recherche(lst,m):
  print(lst) # pour voir la taille de la liste diminuer
  if len(lst) == 1 :  #cas de base
    if lst[0] == m :
      return True
    else :
      return False
  else :              #cas récursif
      mid = len(lst)//2
      if lst[mid] > m :
        return recherche(lst[:mid],m)
      else :
        return recherche(lst[mid:],m)
lst=[5,6,9,12,17]

recherche(lst,18)
```

    [5, 6, 9, 12, 17]
    [9, 12, 17]
    [12, 17]
    [17]





    False



## Exercice 8
On considère le jeu des **Tours de Hanoï**.
Le but est de faire passer toutes les assiettes de A vers C, sachant qu'une assiette ne peut être déposée que sur une assiette de diamètre inférieur.
![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/hanoi0.png?raw=1)

Une version jouable en ligne peut être trouvée [ici](http://www.dynamicdrive.com/dynamicindex12/towerhanoi.htm).

1. S'entraîner et essayer d'établir une stratégie de victoire.
2. Observer les images ci-dessous :
![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/hanoi1.png?raw=1)
![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/hanoi2.png?raw=1)
![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/hanoi3.png?raw=1)
![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/hanoi4.png?raw=1)


Écrire une fonction récursive ```hanoi(n, A, B, C)``` qui donnera la suite d'instructions (sous la forme " A vers C") pour faire passer une pile de taille n de A vers C en prenant B comme intermédiaire.


```python
def hanoi(n,A,B,C):
  """ n : nombre d'assiettes dans la pile
  # A : la pile de départ("A", "B" ou "C")
  # B : la pile intermédaire("A", "B" ou "C")
  # C : la pile d'arrivée ("A", "B" ou "C") """

  if n == 1 :
    print(A + " vers " + C)
  else :
    hanoi(n-1,A,C,B) #de A vers B en passant par C
    print(A + " vers " + C)
    hanoi(n-1,B,A,C)

hanoi(5,"Tower1","Tower2","Tower3")
```

    Tower1 vers Tower3
    Tower1 vers Tower2
    Tower3 vers Tower2
    Tower1 vers Tower3
    Tower2 vers Tower1
    Tower2 vers Tower3
    Tower1 vers Tower3
    Tower1 vers Tower2
    Tower3 vers Tower2
    Tower3 vers Tower1
    Tower2 vers Tower1
    Tower3 vers Tower2
    Tower1 vers Tower3
    Tower1 vers Tower2
    Tower3 vers Tower2
    Tower1 vers Tower3
    Tower2 vers Tower1
    Tower2 vers Tower3
    Tower1 vers Tower3
    Tower2 vers Tower1
    Tower3 vers Tower2
    Tower3 vers Tower1
    Tower2 vers Tower1
    Tower2 vers Tower3
    Tower1 vers Tower3
    Tower1 vers Tower2
    Tower3 vers Tower2
    Tower1 vers Tower3
    Tower2 vers Tower1
    Tower2 vers Tower3
    Tower1 vers Tower3


## Exercice 9

Cet exercice a pour objectif le tracé du flocon de Von Koch.
![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/floc.png?raw=1)


L'idée est de répéter de manière récursive la transformation ci-dessous : chaque segment de longueur ```l``` donne naissance à 4 segments de longueur ```l/3```, en construisant une pointe de triangle équilatéral sur le deuxième tiers du segment.

![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/ex2.png?raw=1)



1) Créer une fonction récursive ```floc(n,l)``` qui trace à une «profondeur» ```n``` un segment de longueur ```l```.
![](https://github.com/glassus/nsi/blob/master/Terminale/Theme_2_Programmation/2.2_Recursivite/data/ex3b.png?raw=1)

**Indications**  
    - l'instruction de tracé n'a lieu que quand ```n``` vaut 0.  
    - l'étape ```n``` fait 4 appels sucessifs à l'étape ```n-1```.  

2) Créer une fonction ```triangle(n,l)``` qui trace le flocon complet.


```python
from turtle import *

def floc(n,l):
    if n == 0 :
        forward(l)
    else :
        floc(n-1,l/3)
        left(60)
        floc(n-1,l/3)
        right(120)
        floc(n-1,l/3)
        left(60)
        floc(n-1,l/3)

def triangle(n,l):
    for _ in range(3):
        floc(n,l)
        right(120)

speed(0)
triangle(4,150)
    

```





---
## Bibliographie
- Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
- Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.


---

![](data/ccbysa.png "image") G.Lassus, Lycée François Mauriac --  Bordeaux  



```python

```
