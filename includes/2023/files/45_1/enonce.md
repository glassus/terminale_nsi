On veut trier par ordre croissant les notes d’une évaluation qui sont des nombres entiers
compris entre 0 et 10 (inclus).

Ces notes sont contenues dans une liste `notes_eval`.

Écrire une fonction `rangement_valeurs` prenant en paramètre la liste `notes_eval` et
renvoyant une liste de longueur 11 telle que la valeur de cette liste à chaque rang est
égale au nombre de notes valant ce rang. Ainsi le terme de rang 0 indique le nombre de
note 0, le terme de rang 1 le nombre de note 1, etc.

Écrire ensuite une fonction `notes_triees` prenant en paramètre la liste des effectifs
des notes et renvoyant une liste contenant la liste, triée dans l’ordre croissant, des notes
des élèves.

Exemple :

```python
>>> notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

>>> effectifs_notes = rangement_valeurs(notes_eval)
>>> effectifs_notes
[2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]

>>> notes_triees(effectifs_notes)
[0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
```