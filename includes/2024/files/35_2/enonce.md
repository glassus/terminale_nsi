Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à
gauche : *bob*, *radar*, et *non* sont des mots palindromes.

De même certains nombres sont eux aussi des palindromes : 33, 121, 345543.

L’objectif de cet exercice est d’obtenir un programme Python permettant de tester si un
nombre est un nombre palindrome.

Pour remplir cette tâche, on vous demande de compléter le code des trois fonctions ci-
dessous sachant que la fonction `est_nbre_palindrome` s’appuiera sur la fonction
`est_palindrome` qui elle-même s’appuiera sur la fonction `inverse_chaine`.

La fonction `inverse_chaine` inverse l'ordre des caractères d'une chaîne de caractères
`chaine` et renvoie la chaîne inversée.

La fonction `est_palindrome` teste si une chaine de caractères `chaine` est un
palindrome. Elle renvoie `True` si c’est le cas et `False` sinon. Cette fonction s’appuie sur
la fonction précédente.

La fonction `est_nbre_palindrome` teste si un nombre `nbre` est un palindrome. Elle
renvoie `True` si c’est le cas et `False` sinon. Cette fonction s’appuie sur la fonction
précédente.

Compléter le code des trois fonctions ci-dessous.

```python linenums='1'
def inverse_chaine(chaine):
    result = ...
    for caractere in chaine:
        result = ...
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return ...

def est_nbre_palindrome(nbre):
    chaine = ...
    return est_palindrome(chaine)
```
Exemples :

```python
>>> inverse_chaine('bac')
'cab'
>>> est_palindrome('NSI')
False
>>> est_palindrome('ISN-NSI')
True
>>> est_nbre_palindrome(214312)
False
>>> est_nbre_palindrome(213312)
True
```