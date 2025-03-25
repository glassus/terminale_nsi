Écrire une fonction `recherche_motif` qui prend en paramètre une chaîne de caractères
`motif` non vide et une chaîne de caractères `texte` et qui renvoie la liste des positions de
`motif` dans `texte`. Si `motif` n’apparaît pas, la fonction renvoie une liste vide.

Exemples:

```python
>>> recherche_motif("ab", "")
[]
>>> recherche_motif("ab", "cdcdcdcd")
[]
>>> recherche_motif("ab", "abracadabra")
[0, 7]
>>> recherche_motif("ab", "abracadabraab")
[0, 7, 11]
```
