Sur le réseau social TipTop, on s’intéresse au nombre de « like » des abonnés.
Les données sont stockées dans des dictionnaires où les clés sont les pseudos et les valeurs
correspondantes sont les nombres de « like » comme ci-dessous :


`{'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}`


Écrire une fonction `max_dico` qui :

- Prend en paramètre un dictionnaire `dico` non vide dont les clés sont des chaînes de
caractères et les valeurs associées sont des entiers ;
- Renvoie un tuple dont :
    - La première valeur est la clé du dictionnaire associée à la valeur maximale ;
    - La seconde valeur est la première valeur maximale présente dans le
dictionnaire.

Exemples :

```python
>>> max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})
('Ada', 201)
>>> max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50})
('Alan', 222)
```