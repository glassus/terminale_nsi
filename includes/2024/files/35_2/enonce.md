Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à gauche :
*kayak*, *radar*, et *non* sont des mots palindromes.

De même certains nombres ont des écritures décimales qui sont des palindromes : 33, 121,
345543.


L’objectif de cet exercice est d’obtenir un programme Python permettant de tester si un
nombre est un nombre palindrome.

Pour remplir cette tâche, on vous demande de compléter le code des trois fonctions ci-
dessous qui s’appuient les unes sur les autres :

- `inverse_chaine` : qui renvoie une chaîne de caractères inversée ;
- `est_palindrome` : qui teste si une chaîne de caractères est un palindrome ;
- `est_nbre_palindrome` : qui teste si un nombre est un palindrome.


Compléter le code des trois fonctions ci-dessous.
```python linenums='1'
def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ... 
    for caractere in chaine:
        resultat = ... 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return ... 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
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