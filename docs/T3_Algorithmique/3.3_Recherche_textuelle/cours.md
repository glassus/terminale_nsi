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

Exemple d'utilisation :
```python
>>> recherche_naive("une magnifique maison bleue", "maison")
[15]
>>> recherche_naive("une magnifique maison bleue", "nsi")
[]
>>> recherche_naive("une magnifique maison bleue", "ma")
[4, 15]
```


### 1.2 Modification de l'algorithme

!!! example "Exercice 1"
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

Nous allons travailler avec le Tome 1 du roman _Les Misérables_ de Victor Hugo, à télécharger [ici](data/Les_Miserables.txt){. target="_blank"} :arrow_down: au format ```txt```. 

#### 1.3.1 Récupération du texte dans une seule chaîne de caractères

```python linenums='1'
with open("Les_Miserables.txt") as f:
    roman = f.read().replace('\n', ' ')
```

#### 1.3.2 Vérification et mesure du temps de recherche

!!! example "Exercice 2"
    === "Énoncé"
        À l'aide du module ```time```, mesurer le temps de recherche dans Les Misérables d'un mot court, d'une longue phrase (présente dans le texte), d'un mot qui n'existe pas. Que remarquez-vous ?  
    === "Correction"
        ```python
        t0 = time.time()
        motif = "maison"
        print(recherche_naive(roman, motif))
        print(time.time()-t0)

        t0 = time.time()
        motif = "La chandelle était sur la cheminée et ne donnait que peu de clarté."
        print(recherche_naive(roman, motif))
        print(time.time()-t0)

        t0 = time.time()
        motif = "parcoursup"
        print(recherche_naive(roman, motif))
        print(time.time()-t0)
        ```
        
        retour console :

        ```python
        [7264, 9090, 9547, 9745, 10936, 17820, 23978, 38192, 41639, 41651, 41840, 42493, 48028, 48393, 51448, 53353, 70867, 72692, 72768, 75608, 77855, 108489, 115739, 130629, 132983, 138870, 143681, 144600, 153114, 155973, 158709, 160700, 163649, 169164, 169181, 171761, 171967, 182642, 186413, 190534, 219378, 220314, 224518, 225098, 227579, 296302, 345108, 345893, 346740, 349677, 359727, 362025, 389945, 395690, 434118, 438068, 457795, 457886, 464696, 469403, 501768, 514980, 520667, 520878, 520926, 520968, 522707, 529329, 598128, 601390, 645915]
        0.21963715553283691
        [651731]
        0.21761441230773926
        []
        0.22150230407714844
        ```

        On remarque que le temps de recherche est semblable, quel que soit le motif cherché. 


## 2. Algorithme de Boyer-Moore-Horspool

???+ tip "Illustration de l'algorithme"
    <gif-player src="https://glassus.github.io/terminale_nsi/T3_Algorithmique/3.3_Recherche_textuelle/data/gif_BM.gif" speed="1" play></gif-player>

    _Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._

### 2.1 Principe

### 2.2 Implémentation
