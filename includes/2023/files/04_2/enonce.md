On souhaite générer des grilles du jeu de démineur à partir de la position des bombes à
placer.  
On se limite à la génération de grilles carrées de taille $n \times n$ où $n$ est le nombre de bombes du jeu.  

Dans le jeu du démineur, chaque case de la grille contient soit une bombe, soit une valeur
qui correspond aux nombres de bombes situées dans le voisinage direct de la case (au-
dessus, en dessous, à droite, à gauche ou en diagonale : chaque case a donc 8 voisins si
elle n'est pas située au bord de la grille).

Voici un exemple de grille $5 \times 5$ de démineur dans laquelle la bombe est représentée par une étoile :

![image](data2023/04grille.png){: .center}


On utilise une liste de listes pour représenter la grille et on choisit de coder une bombe par la valeur -1.

L'exemple ci-contre sera donc codé par la liste :

```python
[[1, 1, 1, 0, 0],
[1, -1, 1, 1, 1]
[2, 2, 3, 2, -1]
[1, -1, 2, -1, 3]
[1, 1, 2, 2, -1]]
```

Compléter le code suivant afin de générer des grilles de démineur, on pourra vérifier que
l’instruction `genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)])`
produit bien la liste donnée en exemple.


