On considère un tableau d'entiers `tab` (de type `list`) dont les éléments sont des `0` ou des `1`). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri, le tableau est constitué de trois zones consécutives, la première ne contenant que des `0`,
la seconde n'étant pas triée et la dernière ne contenant que des `1`.

<table>
<tr>
<td>Zone de 0</td><td>Zone non triée</td><td>Zone de 1</td>
</tr>
</table>

Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier
élément :

- si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant
que des 0 ;
- si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on
considère alors qu’il appartient à la zone ne contenant que des 1.

Dans tous les cas, la longueur de la zone non triée diminue de 1.

Recopier sous Python en la complétant la fonction `tri` suivante :

```python linenums='1'
def tri(tab):
    # i est le premier indice de la zone non triée,
    # j est le dernier indice de cette zone non triée.
    # Au début, la zone non triée est le tableau complet.
    i = ...
    j = ...
    while i != j:
        if tab[i]== 0:
            i = ...
        else:
            valeur = tab[j]
            tab[j] = ...
            ...
            j = ...
    ...
```

Exemple :
```python
>>> tri([0,1,0,1,0,1,0,1,0])
[0, 0, 0, 0, 0, 1, 1, 1, 1]       
```