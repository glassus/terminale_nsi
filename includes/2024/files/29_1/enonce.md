Écrire une fonction `moyenne(notes)` qui renvoie la moyenne pondérée des
résultats contenus dans le tableau `notes`, non vide, donné en paramètre. Ce
tableau contient des couples `(note, coefficient)` dans lesquels :

- `note` est un nombre de type flottant (`float`) compris entre 0 et 20 ;
- `coefficient` est un nombre entier strictement positif.

Ainsi l’expression `moyenne([(15.0,2),(9.0,1),(12.0,3)])` devra renvoyer `12.5`.

$\dfrac{2 \times 15 + 1 \times 9 + 3 \times 12 }{2+1+3}=12,5$