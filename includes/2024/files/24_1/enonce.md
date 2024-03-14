Un arbre binaire est soit vide, représenté en Python par la valeur `None`, soit un nœud
représenté par un triplet `(g, x, d)` où `x` est l’étiquette du nœud et `g` et `d` sont les sous-arbres gauche et droit.

On souhaite écrire une fonction `parcours_largeur` qui prend en paramètre un arbre
binaire et qui renvoie la liste des étiquettes des nœuds de l’arbre parcourus en largeur.

Exemples :

```python
>>> arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )
>>> parcours_largeur(arbre)
[4, 2, 6, 1, 3, 5, 7]
```