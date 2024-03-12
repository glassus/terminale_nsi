On s’intéresse à la suite d’entiers définie par :

- les deux premiers termes sont égaux à 1,
- ensuite, chaque terme est obtenu en faisant la somme des deux termes qui le
précèdent.

En mathématiques, on le formule ainsi :

$U_1 = 1$, $U_2 = 1$ et, pour tout entier naturel non nul $n$, par $U_{n+2} = U_{n+1} + U_n$.

Cette suite est connue sous le nom de suite de Fibonacci.  
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
>>> fibonacci(45)
1134903170
```