Le nombre d’occurrences d’un caractère dans une chaîne de caractère est le nombre
d’apparitions de ce caractère dans la chaîne.

Exemples :

- le nombre d’occurrences du caractère ‘o’ dans ‘bonjour’ est 2 ;
- le nombre d’occurrences du caractère ‘b’ dans ‘Bébé’ est 1 ;
- le nombre d’occurrences du caractère ‘B’ dans ‘Bébé’ est 1 ;
- le nombre d’occurrences du caractère ‘ ‘ dans ‘Hello world !’ est 2.

On cherche les occurrences des caractères dans une phrase. On souhaite stocker ces
occurrences dans un dictionnaire dont les clefs seraient les caractères de la phrase et
les valeurs l’occurrence de ces caractères.


Par exemple : avec la phrase 'Hello world !' le dictionnaire est le suivant :

`{'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}`

*L’ordre des clefs n’a pas d’importance.*

Écrire une fonction `nbr_occurrences` prenant comme paramètre une chaîne de
caractères `chaine` et renvoyant le dictionnaire des nombres d’occurrences des
caractères de cette chaîne.