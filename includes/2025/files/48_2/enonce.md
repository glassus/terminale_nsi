On considère dans cet exercice la suite de nombre suivante : 1, 11, 21, 1211, 111221, ...

Cette suite est construite ainsi : pour passer d’une valeur à la suivante, on la lit et on l’écrit sous la forme d’un nombre. Ainsi, pour 1211 :

- on lit *un 1, un 2, deux 1* ;
- on écrit donc en nombre *1 1, 1 2, 2 1* ;
- puis on concatène *111221*.

Compléter la fonction `nombre_suivant` qui prend en entrée un nombre sous forme de
chaine de caractères et qui renvoie le nombre suivant par ce procédé, encore sous forme de
chaîne de caractères.

```python linenums='1'
def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(...): 
        if s[i] == chiffre:
            compte = ... 
        else:
            resultat += ... + ... 
            chiffre = ... 
            ...
    lecture_... = ... + ... 
    resultat += lecture_chiffre
    return resultat

```

Exemples :

```python
>>> nombre_suivant('1211')
'111221'
>>> nombre_suivant('311')
'1321'
```