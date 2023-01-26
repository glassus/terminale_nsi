On s’intéresse à la suite d’entiers définie par
`U1 = 1`, `U2 = 1` et, pour tout entier naturel `n`, par `Un+2 = Un+1 + Un`.

Elle s’appelle la suite de Fibonacci.

Écrire la fonction `fibonacci` qui prend un entier `n > 0` et qui renvoie l’élément d’indice
`n` de cette suite.

On utilisera une programmation dynamique (pas de récursivité).

Exemple :

```python
>>> fibonacci(1)
1
>>> fibonacci(2)
1
>>> fibonacci(25)
75025
>>> fibonacci(45)
1134903170
```