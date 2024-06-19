### Exercice 1

**Q1.** ```s2``` n'a aucun prédécesseur donc son attribut ```predecesseurs``` est une liste vide.

**Q2.** 
```python linenums='11'
s4.predecesseurs = [(s1, 1), (s2, 2)]
s5.predecesseurs = [(s1, 2), (s3, 3), (s4, 6)]
```

**Q3.** Cela renvoie la valeur 5, qui est le nombre de liens depuis le site ```site2``` vers le site ```site3```. 

**Q4.** La valeur de popularité de ```site1``` est 6.

**Q5.**
```python linenums='1'
def calculPopularite(self):
    popularite = 0
    for site in self.predecesseurs:
        popularite += site[1]
    return popularite
```

**Q6.** C'est une structure de file.

**Q7.** C'est un parcours en largeur.

**Q8.** La valeur renvoyée est 
```python
[s1, s3, s4, s5]
```

**Q9.**
```python linenums='6'
maxPopularite = site.popularite
siteLePlusPopulaire = site
```

**Q10.**
Cela renverra ```s5```, car le site 5 est le plus populaire avec 9 liens.

**Q11.**
Un parcours de graphe n'est pas forcément adapté, car il ne va étudier que chaque composante connexe du graphe : si les sites présentent deux nuages distincts, il faudra faire deux parcours. De plus, la méthode ```pop(0)``` peut être très lente si la liste est de grande taille. 
