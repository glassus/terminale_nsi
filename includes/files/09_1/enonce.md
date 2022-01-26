Soit un nombre entier supérieur ou égal à 1 :

- s'il est pair, on le divise par 2 ;
- s’il est impair, on le multiplie par 3 et on ajoute 1.

Puis on recommence ces étapes avec le nombre entier obtenu, jusqu’à ce que l’on
obtienne la valeur 1.

On définit ainsi la suite $(U_n)$ par :

- $U_0=k$, où $k$ est un entier choisi initialement;
- $U_{n+1} = \dfrac{U_n}{2}$ si $U_n$ est pair;
- $U_{n+1} = 3 \times U_n + 1$ si $U_n$ est impair.

**On admet que, quel que soit l'entier ```k``` choisi au départ, la suite finit toujours sur la valeur 1.**

Écrire une fonction ```calcul``` prenant en paramètres un entier ```k``` strictement positif et qui renvoie la liste des valeurs de la suite, en partant de ```k``` et jusqu'à atteindre 1.

Exemple :
```python
>>> calcul(7)
[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```