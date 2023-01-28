On considère une piste carrée qui contient 4 cases par côté. Les cases sont numérotées
de 0 inclus à 12 exclu comme ci-dessous :

![image](data2023/20_carre.png){: .center width=20%}

L’objectif de l’exercice est d’implémenter le jeu suivant :

Au départ, le joueur place son pion sur la case 0. A chaque coup, il lance un dé équilibré
à six faces et avance son pion d’autant de cases que le nombre indiqué par le dé (entre
1 et 6 inclus) dans le sens des aiguilles d’une montre.

Par exemple, s’il obtient 2 au premier lancer, il pose son pion sur la case 2 puis s’il
obtient 6 au deuxième lancer, il le pose sur la case 8, puis s’il obtient à nouveau 6, il
pose le pion sur la case 2.

Le jeu se termine lorsque le joueur a posé son pion sur **toutes les cases** de la piste.

Compléter la fonction `nbre_coups` ci-dessous de sorte qu’elle renvoie le nombre de
lancers aléatoires nécessaires pour terminer le jeu.

Proposer ensuite quelques tests pour en vérifier le fonctionnement.

```python linenums='1'
from random import randint

def nbre_coups():
    n = ...
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while ... < ...:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + ...) % ...
        if ...:
            cases_vues.append(case_en_cours)
        n = ...
    return n
```
