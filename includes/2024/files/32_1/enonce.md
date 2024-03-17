L'opérateur « ou exclusif » entre deux bits renvoie 0 si les deux bits sont égaux et 1 s'ils sont
différents. Il est symbolisé par le caractère ⊕.
Ainsi :

- 0 ⊕ 0 = 0
- 0 ⊕ 1 = 1
- 1 ⊕ 0 = 1
- 1 ⊕ 1 = 0  

Écrire une fonction `ou_exclusif` qui prend en paramètres deux tableaux de 0 ou de 1 de
même longueur et qui renvoie un tableau où l’élément situé à position `i` est le résultat, par
l’opérateur « ou exclusif », des éléments à la position `i` des tableaux passés en paramètres.

```python
>>> ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0])
[1, 1, 0, 1, 1, 0, 0, 1]
>>> ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1])
[1, 1, 1, 0]
```