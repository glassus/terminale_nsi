Écrire une fonction `enumere` qui prend en paramètre un tableau `tab` (type `list`) et renvoie
un dictionnaire `d` dont les clés sont les éléments de `tab` avec pour valeur associée la liste
des indices de l’élément dans le tableau `tab`.

Exemple :

```python
>>> enumere([])
{}
>>> enumere([1, 2, 3])
{1: [0], 2: [1], 3: [2]}
>>> enumere([1, 1, 2, 3, 2, 1])
{1: [0, 1, 5], 2: [2, 4], 3: [3]}
```