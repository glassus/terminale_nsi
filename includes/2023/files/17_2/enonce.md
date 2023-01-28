On cherche à déterminer les valeurs du triangle de Pascal (Figure 1).

Dans le triangle de Pascal, chaque ligne commence et se termine par le nombre 1.
Comme l’illustre la Figure 2, on additionne deux valeurs successives d’une ligne pour
obtenir la valeur qui se situe sous la deuxième valeur.

![image](data2023/17_triangle.png){: .center width=60%}

Compléter la fonction `pascal` ci-après prenant en paramètre un entier `n` supérieur ou
égal à 2. Cette fonction doit renvoyer une liste correspondant au triangle de Pascal de la
ligne 0 à la ligne `n`. Le tableau représentant le triangle de Pascal sera contenu dans la
variable `triangle`.

```python linenums='1'
def pascal(n):
    triangle = [[1]]
    for k in range(1,...):
        ligne_k = [...]
        for i in range(1,k):
            ligne_k.append(triangle[...][i-1]+triangle[...][...])
        ligne_k.append(...)
        triangle.append(ligne_k)
    return triangle
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
