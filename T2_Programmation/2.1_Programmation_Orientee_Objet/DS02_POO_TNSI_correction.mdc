# DS02 Correction
## Programmation Orientée Objet

### Exercice 1

L'objectif de cet exercice est de créer une classe ```Eleve```.

Chaque objet de cette classe aura 3 attributs, donnés en paramètres dans la méthode constructeur :

- ```nom``` : nom de l'élève, de type ```String```. Exemple : ```'Homer Simpson'``` 
- ```niveau``` : classe de l'élève, de type ```String```. Exemple : ```'TG1'``` 
- ```annee``` : année de naissance de l'élève, de type ```Int```. Exemple : ```2002``` 

Chaque objet de cette classe aura aussi une méthode ```change_niveau()``` qui permet de changer l'attribut ```niveau``` de l'élève.


1. Créer cette classe, avec les trois attributs et la méthode demandés.
2. Instancier deux élèves ```eleve1``` et ```eleve2``` (je vous laisse le choix des différentes valeurs à donner aux attributs).
3. Changer le niveau de ```eleve1``` en utilisant la méthode ```change_niveau()```.
4. Créer une fonction ```plus_vieux(e1, e2)``` qui affiche le nom de l'élève le plus âgé (ou les deux en cas d'égalité), lorsque ```e1``` et ```e2``` sont deux instances de la classe ```Eleve```. 



```python
class Eleve:
    
    def __init__(self, nom, niveau, annee):
        self.nom = nom
        self.niveau = niveau
        self.annee = annee
        
    def change_niveau(self, nouveau_niveau):
        self.niveau = nouveau_niveau
```


```python
eleve1 = Eleve("Bart", "CM2", 2010)
eleve2 = Eleve("Lisa", "CM1", 2009)
```


```python
eleve1.niveau
```




    'CM2'




```python
eleve1.change_niveau("6eme")
```


```python
eleve1.niveau
```




    '6eme'




```python
def plus_vieux(e1, e2):
    if e1.annee >= e2.annee:
        print(e2.nom)
    else:
        print(e1.nom)
        
plus_vieux(eleve1, eleve2)
```

    Lisa


________

### Exercice 2

L'objectif de cet exercice est de créer une classe ```Domino``` pour pouvoir créer des dominos :

![image](data/domino.png)

On rappelle qu'un domino comporte deux faces, que nous appellerons ```faceA``` et ```faceB```, et que sur chaque face est indiqué un nombre de points compris entre 1 et 6.

Chaque objet de cette classe ```Domino```  aura pour 2 attributs, donnés en paramètres dans la méthode constructeur :

- ```faceA``` : nombre de points de la face A, de type ```Int```. Exemple : ```3``` 
- ```faceB``` : nombre de points de la face B, de type ```Int```. Exemple : ```4``` 

Chaque objet de cette classe aura aussi une méthode ```dessine()```, qui représentera schématiquement le domino.
Ainsi le domino en photo ci-dessus serait représenté comme ceci :
```
---------
| 3 | 4 |
---------
```  

1. Créer la classe ```Domino```. Instancier un domino ```d1 = Domino(2,5)``` et afficher ce domino ```d1```.  


```python
class Domino:
    
    def __init__(self, faceA, faceB):
        self.faceA = faceA
        self.faceB = faceB
        
    def dessine(self):
        print("---------")
        print("|", self.faceA, "|", self.faceB, "|")
        print("---------") 
```


```python
d1 = Domino(2,5)
d1.dessine()
```

    ---------
    | 2 | 5 |
    ---------


2. Créer une variable ```sac``` qui contiendra 10 dominos de valeurs aléatoires.


```python
from random import randint
sac = [Domino(randint(1, 6), randint(1, 6)) for _ in range(10)]
```

3. Créer une fonction ```sont_compatibles(d1, d2)``` qui prend en paramètres deux objets ```d1``` et ```d2``` de type ```Domino``` et qui renvoie un booléen ```True``` ou ```False```, selon que ces dominos peuvent être assemblés ou non. Pour rappel deux dominos peuvent s'assembler s'ils ont une face identique. Instancier ensuite 3 dominos différents et tester la fonction ```sont_compatibles()```


```python
def sont_compatibles(d1, d2):
    if d1.faceA == d2.faceA or d1.faceA == d2.faceB:
        return True
    if d1.faceB == d2.faceA or d1.faceB == d2.faceB:
        return True
    return False

d1 = Domino(2,4)
d2 = Domino(2,6)
d3 = Domino(3,5)
```


```python
sont_compatibles(d1,d2)
```




    True




```python
sont_compatibles(d1,d3)
```




    False



4. Créer une fonction ```trouve_jouables(d)``` qui prend un paramètre un objet ```d``` de type ```Domino``` et qui dessine tous les dominos de ```sac``` qui peuvent être assemblés avec ```d```.  


```python
def trouve_jouable(d):
    for domino in sac:
        if sont_compatibles(d, domino):
            domino.dessine()
```


```python
trouve_jouable(d1)
```

    ---------
    | 4 | 4 |
    ---------
    ---------
    | 2 | 6 |
    ---------
    ---------
    | 4 | 6 |
    ---------
    ---------
    | 2 | 3 |
    ---------


________
