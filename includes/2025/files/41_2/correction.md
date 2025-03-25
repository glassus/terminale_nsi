```python linenums='1' hl_lines='29-31 34-36 38'
class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False

        #test de la somme de chaque colonne
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True
```

Tests avec :

```python linenums='1'
lst_c2 = [1, 7, 7, 1]
lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
lst_c3bis = [2, 9, 4, 7, 0, 3, 6, 1, 8]
```

```python
>>> c2 = Carre(lst_c2, 2)
>>> c2.est_semimagique()
True

>>> c3 = Carre(lst_c3, 3)
>>> c3.est_semimagique()
True

>>> c3bis = Carre(lst_c3bis, 2)
>>> c3bis.est_semimagique()
False
```