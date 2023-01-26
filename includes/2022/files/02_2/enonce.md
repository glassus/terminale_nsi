On cherche à déterminer les valeurs du triangle de Pascal. Dans ce tableau de forme
triangulaire, chaque ligne commence et se termine par le nombre 1. Par ailleurs, la valeur
qui occupe une case située à l’intérieur du tableau s’obtient en ajoutant les valeurs des
deux cases situées juste au-dessus, comme l’indique la figure suivante :

![image](data/img9_2t.png){: .center width=60%}

Compléter la fonction `pascal` ci-après. Elle doit renvoyer une liste correspondant au
triangle de Pascal de la ligne `1` à la ligne `n` où `n` est un nombre entier supérieur ou égal à
`2` (le tableau sera contenu dans la variable `C`). La variable `Ck` doit, quant à elle, contenir,
à l’étape numéro `k`, la `k`-ième ligne du tableau.

```python linenums='1'
def pascal(n):
    C= [[1]]
    for k in range(1,...):
        Ck = [...]
        for i in range(1,k):
            Ck.append(C[...][i-1]+C[...][...] )
        Ck.append(...)
        C.append(Ck)
    return C
```

Pour `n = 4`, voici ce qu'on devra obtenir :
```python
>>> pascal(4)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
``` 
Pour `n = 5`, voici ce qu'on devra obtenir :
```python
>>> pascal(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
```
