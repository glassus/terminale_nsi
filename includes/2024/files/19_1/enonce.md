On rappelle que :

- le nombre $a^n$ est le nombre $a \times a \times a \times \dots \times a$, où le facteur $a$ apparaît $n$ fois,
- en langage Python, l’instruction `t[-1]` permet d’accéder au dernier élément du
tableau `t`.


Dans cet exercice, l’opérateur ```**```  et la fonction `pow` ne sont pas autorisés.

Programmer en langage Python une fonction `liste_puissances` qui prend en argument
un nombre entier `a`, un entier strictement positif `n` et qui renvoie la liste de ses puissances
$\rm{[a^1, a^2, ..., a^n]}$.


Programmer également une fonction `liste_puisssances_borne` qui prend en
argument un nombre entier `a` supérieur ou égal à 2 et un entier `borne`, et qui renvoie la
liste de ses puissances, à l’exclusion de $\rm{a^0}$, strictement inférieures à `borne`.

Exemples :

```python
>>> liste_puissances(3, 5)
[3, 9, 27, 81, 243]
>>> liste_puissances(-2, 4)
[-2, 4, -8, 16]
>>> liste_puissances_borne(2, 16)
[2, 4, 8]
>>> liste_puissances_borne(2, 17)
[2, 4, 8, 16]
>>> liste_puissances_borne(5, 5)
[]
```