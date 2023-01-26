Écrire une fonction `tri_selection` qui prend en paramètre une liste `tab` de nombres
entiers et qui renvoie le tableau trié par ordre croissant.

On utilisera l’algorithme suivant :

- on recherche le plus petit élément du tableau, et on l'échange avec l'élément d'indice 0 ;
- on recherche le second plus petit élément du tableau, et on l'échange avec l'élément
d'indice 1 ;
- on continue de cette façon jusqu'à ce que le tableau soit entièrement trié.

Exemple :
```python
>>> tri_selection([1,52,6,-9,12])
[-9, 1, 6, 12, 52]
``` 