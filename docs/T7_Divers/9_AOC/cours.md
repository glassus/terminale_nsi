# Advent Of Code - conseils

![image](data/ban.png){: .center}

## 1. Où mettre les données ?

Je vous conseille de travailler avec 2 fichiers : 

- ```input.txt``` qui contiendra l'input réel qui vous permettra de trouver votre solution.
- ```input_test.txt``` qui contiendra les données de test (qui sont toujours proposées au sein de l'énigme).  

## 2. Comment récupérer et exploiter ces données ?

### 2.1 Récupération des données dans une liste :

L'instruction suivante :

```python linenums='1'
data = open('input_test.txt').read().splitlines()
```

va récupérer au sein d'une liste toutes les lignes de l'input. Attention, les objets contenus dans la liste sont des chaînes de caractères.

Exemple avec le fichier ```input_test.txt```

```python
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```

La variable ```data``` sera alors :
```python
>>> data
['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']
```

### 2.2 Exploiter ces données

Le plus dur commence ! Suivant ce qu'il va falloir faire avec ces données, vous allez devoir les triturer pour les utiliser, au sein de différentes structures (listes, dictionnaires... ).  
Cela dépend des situations. Ici par exemple, les données sont «juste» des nombres, on peut donc parcourir la liste et effectuer un ```int()``` pour les convertir en nombre lorsque c'est nécessaire...  