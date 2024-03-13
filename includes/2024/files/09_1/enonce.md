On veut trier par ordre croissant les notes d’une évaluation qui sont des nombres entiers
compris entre 0 et 10 (inclus).

Ces notes sont contenues dans un tableau `notes_eval` (type `list`)

Écrire une fonction `effectif_notes` prenant en paramètre le tableau `notes_eval` et
renvoyant un tableau de longueur 11 tel que la valeur d’indice `i` soit le nombre de notes
valant `i` dans le tableau `notes_eval`.


Écrire ensuite une fonction `notes_triees` prenant en paramètre le tableau des effectifs
des notes et renvoyant un tableau contenant les mêmes valeurs que `notes_eval` mais
triées dans l’ordre croissant.


Exemple :

```python
>>> notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
>>> eff = effectif_notes(notes_eval)
>>> eff
[2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
>>> notes_triees(eff)
[0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
```