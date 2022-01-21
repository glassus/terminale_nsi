Écrire une fonction `conv_bin` qui prend en paramètre un entier positif `n` et renvoie un
couple (`b,bit)` où :

- `b` est une liste d'entiers correspondant à la représentation binaire de `n`;
- `bit` correspond aux nombre de bits qui constituent `b`.

Exemple :
```python
>>> conv_bin(9)
([1,0,0,1],4)
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