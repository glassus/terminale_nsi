Écrire une fonction `a_doublon` qui prend en paramètre un tableau **trié** de nombres dans
l’ordre croissant et renvoie `True` si ce tableau contient au moins deux nombres identiques,
`False` sinon.

Exemple :

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