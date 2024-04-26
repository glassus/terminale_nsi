On s’intéresse à la suite d’entiers définie par :

- les deux premières valeurs sont égales à 1 ;
- ensuite, chaque valeur est obtenue en faisant la somme des deux valeurs qui la précè-
dent.

La troisième valeur est donc $1+1 = 2$, la quatrième est $1+2 = 3$, la cinquième est $2+3 = 5$,
la sixième est $3 + 5 = 8$, et ainsi de suite.

Cette suite d’entiers est connue sous le nom de suite de Fibonacci.

Écrire en Python une fonction `fibonacci` qui prend en paramètre un entier `n` supposé
strictement positif et qui renvoie le terme d’indice `n` de cette suite.

Exemples :

```python
>>> fibonacci(1)
1
>>> fibonacci(2)
1
>>> fibonacci(25)
75025
```