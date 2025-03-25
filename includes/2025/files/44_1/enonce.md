Dans cet exercice on cherche à calculer la moyenne pondérée d’un élève dans une matière
donnée. Chaque note est associée à un coefficient qui la pondère.


Par exemple, si ses notes sont : 14 avec coefficient 3, 12 avec coefficient 1 et 16 avec coeffi-
cient 2, sa moyenne pondérée sera donnée par

$$\dfrac{14 \times 3 + 12 \times 1 + 16 \times 2}{3+1+2}=14,333... $$


Écrire une fonction `moyenne` :

- qui prend en paramètre une liste notes non vide de tuples à deux éléments entiers
de la forme `(note, coefficient)` (`int` ou `float`) positifs ou nuls ;
- et qui renvoie la moyenne pondérée des notes de la liste sous forme de flottant si la
somme des coefficients est non nulle, `None` sinon.


Exemple :

```python
>>> moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
9.142857142857142
>>> moyenne([(3, 0), (5, 0)])
None
```
