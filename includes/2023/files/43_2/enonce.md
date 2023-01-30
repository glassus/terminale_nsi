La fonction `tri_bulles` prend en paramètre une liste `T` d’entiers non triés et renvoie la
liste triée par ordre croissant.


Le tri à bulles est un tri en place qui commence par placer le plus grand élément en
dernière position en parcourant la liste de gauche à droite et en échangeant au passage
les éléments voisins mal ordonnés (si la valeur de l’élément d’indice `i` a une valeur
strictement supérieure à celle de l’indice `i + 1`, ils sont échangés). Le tri place ensuite
en avant-dernière position le plus grand élément de la liste privée de son dernier élément
en procédant encore à des échanges d’éléments voisins. Ce principe est répété jusqu’à
placer le minimum en première position.


Exemple : pour trier la liste `[7, 9, 4, 3]` :

- première étape : 7 et 9 ne sont pas échangés, puis 9 et 4 sont échangés, puis 9 et
3 sont échangés, la liste est alors `[7, 4, 3, 9]`
- deuxième étape : 7 et 4 sont échangés, puis 7 et 3 sont échangés, la liste est
alors `[4, 3, 7, 9]`
- troisième étape : 4 et 3 sont échangés, la liste est alors `[3, 4, 7, 9]`


Compléter le code Python ci-dessous qui implémente la fonction tri_bulles.

```python linenums='1'
def tri_bulles(T):
    '''
	Renvoie le tableau T trié par ordre croissant
	'''
    n = len(T)
    for i in range(...,...,-1):
        for j in range(i):
            if T[j] > T[...]:
                ... = T[j]
                T[j] = T[...]
                T[j+1] = temp
    return T


```

Exemples :
```python
>>> tri_bulles([])
[]
>>> tri_bulles([7])
[7]
>>> tri_bulles([9, 3, 7, 2, 3, 1, 6])
[1, 2, 3, 3, 6, 7, 9]
>>> tri_bulles([9, 7, 4, 3])
[3, 4, 7, 9]
```
