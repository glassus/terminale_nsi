# Recherche textuelle
![image](data/illus.png){: .center width=40%}


![image](data/BO.png){: .center}

<!--
<gif-player src="https://glassus.github.io/terminale_nsi/T3_Algorithmique/3.3_Recherche_textuelle/data/gif_naive.gif" speed="1" play></gif-player>

-->

## 1. Recherche naïve

???+ tip "Illustration de l'algorithme"
    <gif-player src="https://glassus.github.io/terminale_nsi/T3_Algorithmique/3.3_Recherche_textuelle/data/gif_naive.gif" speed="1" play></gif-player>

    _Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._

### 1.1 Premier algorithme

!!! note "Algorithme de recherche naïve :heart:"
    ```python linenums='1'
        def recherche_naive(texte, motif):
            '''
            renvoie la liste des indices (éventuellement vide) des occurrences de
            de la chaîne motif dans la chaîne texte.
            '''
            indices = []
            i = 0
            while i <= len(texte) - len(motif):
                k = 0
                while k < len(motif) and texte[i+k] == motif[k]:
                    k += 1
                if k == len(motif):
                    indices.append(i)
                i += 1

            return indices

    ```


### 1.2 Modification de l'algorithme

!!! abstract "Exercice 1"
    === "Énoncé"
        Re-écrire l'algorithme précédent en s'arrêtant dès qu'une occurrence de ```motif``` est trouvée dans ```texte```.

        La fonction renverra uniquement un booléen. 
    === "Correction"
        ```python linenums='1'
        def recherche_naive_bool(texte, motif):
            '''
            renvoie un booléen indiquant la présence ou non de
            la chaîne motif dans la chaîne texte.
            '''
            trouve = False
            i = 0
            while i <= len(texte) - len(motif) and not trouve:
                k = 0
                while k < len(motif) and texte[i+k] == motif[k]:
                    k += 1
                if k == len(motif):
                    trouve = True
                i += 1

            return trouve
        ```
         

### 1.3 Application à la recherche d'un motif dans un roman

Le [Projet Gutenberg](https://www.gutenberg.org/browse/languages/fr){. target="_blank"} permet de télécharger légalement des ouvrages libres de droits dans différents formats.

Nous allons travailler avec le Tome 1 du roman _Les Misérables_ de Victor Hugo, à télécharger [ici](data/Les_Miserables.txt){. target="_blank"} au format ```txt```. 

#### 1.3.1 Récupération du texte dans une seule chaîne de caractères

```python linenums='1'
with open("Les_Miserables.txt") as f:
    texte = f.read().replace('\n', ' ')
```

#### 1.3.2 Vérification et mesure du temps de recherche

!!! abstract "Exercice 2"
    === "Énoncé"
        1. Testez la validité de vos réponses en comparant avec les résultats donnés par la fonctionnalité ```Ctrl-F``` proposée par votre navigateur
        2. Mesurez le temps d'exécution de votre algorithme à l'aide du module ```time```.  
    === "Correction"
         


## 2. Algorithme de Boyer-Moore-Horspool

???+ tip "Illustration de l'algorithme"
    <gif-player src="https://glassus.github.io/terminale_nsi/T3_Algorithmique/3.3_Recherche_textuelle/data/gif_BM.gif" speed="1" play></gif-player>

    _Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._

### 2.1 Principe

### 2.2 Implémentation
