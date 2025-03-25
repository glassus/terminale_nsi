On a relevé les valeurs moyennes annuelles des températures à Paris pour la période
allant de 2013 à 2019. Les résultats ont été récupérés sous la forme de deux tableaux (de type
`list`) : l’un pour les températures, l’autre pour les années :

```python
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
```

Écrire la fonction `annee_temperature_minimale` qui prend en paramètres ces deux
tableaux et qui renvoie la plus petite valeur relevée au cours de la période et l’année correspondante.

On suppose que la température minimale est atteinte une seule fois.

Exemple :
```python
>>> annee_temperature_minimale(t_moy, annees)
(12.5, 2016)
```