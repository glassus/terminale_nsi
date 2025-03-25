Écrire une fonction `tri_selection` qui prend en paramètre un tableau `tab` de nombres
entiers (type `list`) et qui le modifie afin qu’il soit trié par ordre croissant.

On utilisera l’algorithme suivant :

- on recherche le plus petit élément du tableau, en le parcourant du rang 0 au dernier
rang, et on l’échange avec l’élément d’indice 0 ;
- on recherche ensuite le plus petit élément du tableau restreint du rang 1 au dernier
rang, et on l’échange avec l’élément d’indice 1 ;
- on continue de cette façon jusqu’à ce que le tableau soit entièrement trié.

Exemple :
```python
>>> tab = [1, 52, 6, -9, 12]
>>> tri_selection(tab)
>>> tab
[-9, 1, 6, 12, 52]
``` 