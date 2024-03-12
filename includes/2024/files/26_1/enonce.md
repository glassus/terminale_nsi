Écrire une fonction `ajoute_dictionnaires` qui prend en paramètres deux
dictionnaires `d1` et `d2` dont les clés sont des nombres et renvoie le dictionnaire `d` défini de
la façon suivante :

- Les clés de `d` sont celles de `d1` et celles de `d2` réunies.
- Si une clé est présente dans les deux dictionnaires `d1` et `d2`, sa valeur associée
dans le dictionnaire d est la somme de ses valeurs dans les dictionnaires `d1` et `d2`.
- Si une clé n’est présente que dans un des deux dictionnaires, sa valeur associée
dans le dictionnaire `d` est la même que sa valeur dans le dictionnaire où elle est
présente.

Exemples :

```python
>>> ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11})
{1: 5, 2: 16, 3: 11}
>>> ajoute_dictionnaires({}, {2: 9, 3: 11})
{2: 9, 3: 11}
>>> ajoute_dictionnaires({1: 5, 2: 7}, {})
{1: 5, 2: 7}
```