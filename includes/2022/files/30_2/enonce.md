Les chiffres romains sont un système ancien d’écriture des nombres.


Les chiffres romains sont: I, V, X, L, C, D, et M.
Ces symboles représentent respectivement 1, 5, 10, 50, 100, 500, et 1000 en base dix.


Lorsque deux caractères successifs sont tels que le caractère placé à gauche possède une
valeur supérieure ou égale à celui de droite, le nombre s’obtient en additionnant le caractère de
gauche à la valeur de la chaîne située à droite.

Ainsi, "XVI" est le nombre 16 car X + VI = 10 + 6.


Lorsque deux caractères successifs sont tels que le caractère placé à gauche possède une
valeur strictement inférieure à celui de droite, le nombre s’obtient en retranchant le caractère de
gauche à la valeur de la chaîne située à droite.


Ainsi, "CDIII" est le nombre 403 car DIII – C = 503 – 100.


On dispose d’un dictionnaire `dico`, à compléter, où les clés sont les caractères apparaissant
dans l’écriture en chiffres romains et où les valeurs sont les nombres entiers associés en
écriture décimale.


On souhaite créer une fonction récursive `rom_to_dec` qui prend en paramètre une chaîne de
caractères (non vide) représentant un nombre écrit en chiffres romains et renvoyant le nombre
associé en écriture décimale :

```python linenums='1'
def rom_to_dec(nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I":1, "V":5, ...}
    if len(nombre) == 1:
        return ...

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
         ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]
    
        
        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + ...
        else:
            return ...

assert rom_to_dec("CXLII") == 142


```