On considère la fonction `binaire`.
Cette fonction prend en paramètre un entier positif `a` en
écriture décimale et renvoie son écriture binaire sous la forme d’une chaine de caractères.

L’algorithme utilise la méthode des divisions euclidiennes successives comme l’illustre
l’exemple ci-après.

![image](data2023/30_divisions.png){: .center}


Compléter le code de la fonction `binaire`.


```python linenums='1'
def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return ...
    bin_a = ...
    while ... :
        bin_a = ... + bin_a
        a = ...
    return bin_a
```

Exemples :
```python
>>> binaire(83)
'1010011'
>>> binaire(127)
'1111111'
>>> binaire(0)
'0'
```