Le but de cet exercice est d’écrire une fonction récursive `traduire_romain` qui prend
en paramètre une chaîne de caractères, non vide, représentant un nombre écrit en
chiffres romains et qui renvoie son écriture décimale.


Les chiffres romains considérés sont : I, V, X, L, C, D et M. Ils représentent
respectivement les nombres 1, 5, 10, 50, 100, 500, et 1000 en base dix.


On dispose d’un dictionnaire `romains` dont les clés sont les caractères apparaissant
dans l’écriture en chiffres romains et les valeurs sont les nombres entiers associés en
écriture décimale :


`romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}`


Le code de la fonction `traduire_romain` fournie repose sur le
principe suivant :

- la valeur d’un caractère est ajoutée à la valeur du reste de la chaîne si ce
caractère a une valeur supérieure (ou égale) à celle du caractère qui le suit ;

- la valeur d’un caractère est retranchée à la valeur du reste de la chaîne si ce
caractère a une valeur strictement inférieure à celle du caractère qui le suit.

Ainsi, XIV correspond au nombre 10 + 5 - 1 puisque :

- la valeur de X (10) est supérieure à celle de I (1), on ajoute donc 10 à la valeur du
reste de la chaîne, c’est-à-dire IV ;

- la valeur de I (1) est strictement inférieure à celle de V (5), on soustrait donc 1 à
la valeur du reste de la chaîne, c’est-à-dire V.

On rappelle que pour priver une chaîne de caractères de son premier caractère, on
utilisera l’instruction :

`nom_de_variable[1:]`

Par exemple, si la variable `mot` contient la chaîne `"CDI"`, `mot[1:]` renvoie `"DI"`.

```python linenums='1'
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """ Renvoie l’écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return ...
    elif romains[nombre[0]] >= ...
        return romains[nombre[0]] + ...
    else:
        return ...
```

Compléter le code de la fonction `traduire_romain` et le tester.

Exemples :

```python
>>> traduire_romain("XIV")
14
>>> traduire_romain("CXLII")
142
>>> traduire_romain("MMXXIII")
2023
```