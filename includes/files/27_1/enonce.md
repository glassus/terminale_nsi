Dans cet exercice, un arbre binaire de caractères est stocké sous la forme d’un
dictionnaire où les clefs sont les caractères des nœuds de l’arbre et les valeurs, pour
chaque clef, la liste des caractères des fils gauche et droit du nœud.

Par exemple, l’arbre

![image](data/img28_1.png){: .center width=40%}

est stocké dans

```python
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}
```

Écrire une fonction récursive `taille` prenant en paramètres un arbre binaire `arbre`
sous la forme d’un dictionnaire et un caractère `lettre` qui est la valeur du sommet de
l’arbre, et qui renvoie la taille de l’arbre à savoir le nombre total de nœud.
On pourra distinguer les 4 cas où les deux « fils » du nœud sont `''`, le fils gauche
seulement est `''`, le fils droit seulement est `''`, aucun des deux fils n’est `''`.

Exemple :
```python
>>> taille(a, ’F’)
9
``` 