Écrire une fonction `indices_maxi` qui prend en paramètre un tableau non vide de nombre
entiers `tab`, représenté par une liste Python et qui renvoie un tuple (`maxi`, `indices`)
où :

- `maxi` est le plus grand élément du tableau `tab` ;
- `indices` est une liste Python contenant les indices du tableau `tab` où apparaît ce
plus grand élément.


Exemple :
```python
>>> indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
(9, [3, 8])
>>> indices_maxi([7])
(7, [0])
```