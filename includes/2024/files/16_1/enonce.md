Écrire une fonction `ecriture_binaire_entier_positif` qui prend en paramètre un
entier positif `n` et renvoie une liste d'entiers correspondant à l‘écriture binaire de `n`.


Ne pas oublier d’ajouter au corps de la fonction une documentation et une ou plusieurs
assertions pour vérifier les pré-conditions.


Exemples :

```python
>>> ecriture_binaire_entier_positif(0)
[0]
>>> ecriture_binaire_entier_positif(2)
[1, 0]
>>> ecriture_binaire_entier_positif(105)
[1, 1, 0, 1, 0, 0, 1]
```

Aide :

- l'opérateur `//` donne le quotient de la division euclidienne : `5//2` donne `2` ;
- l'opérateur `%` donne le reste de la division euclidienne :` 5%2` donne `1` ;
- `append` est une méthode qui ajoute un élément à une liste existante :
Soit `T=[5,2,4]`, alors `T.append(10)` ajoute `10` à la liste `T`. Ainsi, `T` devient
`[5,2,4,10]`.
- `reverse` est une méthode qui renverse les éléments d'une liste.
Soit `T=[5,2,4,10]`. Après `T.reverse()`, la liste devient `[10,4,2,5]`.

On remarquera qu’on récupère la représentation binaire d’un entier `n` en partant de la gauche en appliquant successivement les instructions :

`b = n%2`

`n = n//2`

répétées autant que nécessaire.