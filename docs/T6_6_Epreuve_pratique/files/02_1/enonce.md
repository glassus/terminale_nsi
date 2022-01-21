Soit le couple (`note`,`coefficient`):

- `note` est un nombre de type flottant (`float`) compris entre 0 et 20 ;
- `coefficient` est un nombre entier positif.

Les résultats aux évaluations d'un élève sont regroupés dans une liste composée de
couples (`note`,`coefficient`).

Écrire une fonction moyenne qui renvoie la moyenne pondérée de cette liste donnée en
paramètre.

Par exemple, l’expression `moyenne([(15,2),(9,1),(12,3)])` devra renvoyer le
résultat du calcul suivant :

$\dfrac{2 \times 15 + 1 \times 9 + 3 \times 12 }{2+1+3}=12,5$