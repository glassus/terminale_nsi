Écrire une fonction `a_doublon` qui prend en paramètre une liste **triée** de nombres et
renvoie `True` si la liste contient au moins deux nombres identiques, `False` sinon.

Par exemple :

```python
>>> a_doublon([])
False
>>> a_doublon([1])
False
>>> a_doublon([1, 2, 4, 6, 6])
True
>>> a_doublon([2, 5, 7, 7, 7, 9])
True
>>> a_doublon([0, 2, 3])
False
```