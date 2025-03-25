Écrire une fonction `max_et_indice` qui prend en paramètre un tableau non vide `tab` de
nombres entiers et qui renvoie la valeur du plus grand élément de ce tableau ainsi que
l’indice de sa première apparition dans ce tableau.

L’utilisation de la fonction native `max` n’est pas autorisée.

Exemples :

```python
>>> max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
(9, 3)
>>> max_et_indice([-2])
(-2, 0)
>>> max_et_indice([-1, -1, 3, 3, 3])
(3, 2)
>>> max_et_indice([1, 1, 1, 1])
(1, 0)
```