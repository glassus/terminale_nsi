Écrire une fonction `moyenne(liste_notes)` qui renvoie la moyenne pondérée des
résultats contenus dans la liste `liste_notes`, non vide, donnée en paramètre. Cette
liste contient des couples `(note, coefficient)` dans lesquels :

- `note` est un nombre de type flottant (`float`) compris entre 0 et 20 ;
- `coefficient` est un nombre entier strictement positif.

Ainsi l’expression `moyenne([(15,2),(9,1),(12,3)])` devra renvoyer `12.5`.

$\dfrac{2 \times 15 + 1 \times 9 + 3 \times 12 }{2+1+3}=12,5$