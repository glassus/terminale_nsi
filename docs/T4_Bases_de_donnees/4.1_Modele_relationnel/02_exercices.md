# Exercices sur le modèle relationnel

## Exercice 1
*(d'après Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.)*

Deux relations modélisent la flotte de voitures d'un réseau de location de voitures.

**Agences**

| id_agence | ville     | département |
|-----------|-----------|-------------|
| 1         | Paris     | 75          |
| 2         | Lyon      | 69          |
| 3         | Marseille | 13          |
| 4         | Aubagne   | 13          |


**Voitures**

| id_voiture | marque  | modèle | kilométrage | couleur | id_agence |
|------------|---------|--------|-------------|---------|-----------|
| 1          | Renault | Clio   | 12000       | Rouge   | 2         |
| 2          | Peugeot | 205    | 22000       | Noir    | 3         |
| 3          | Toyota  | Yaris  | 33000       | Noir    | 3         |


!!! example "Questions"
    === "Énoncé"
        1. Combien la relation ```Voitures``` comporte-t-elle d'attributs ?
        2. Que vaut son cardinal ?
        3. Quel est le domaine de l'attribut ```ig_agence```  dans la relation ```Voitures``` ?
        4. Quel est le schéma relationnel de la relation ```Agences ``` ?
        5. Quelle est la clé primaire de la relation ```Agences ``` ?
        6. Quelle est la clé primaire de la relation ```Voitures ``` ?
        7. Quelle est la clé étrangère de la relation ```Voitures ``` ?

    === "Correction"
        {{ correction(True,
        "
        1. 6
        2. 6
        3. Entier (```Int``` )
        5. ```id_agence``` 
        6. ```id_voiture``` 
        7. ```id_agence``` 
        "
        ) }}



## Exercice 2

Reprenons la base Tour de France 2020 vue en cours :


**relation Équipes**

| codeEquipe | nomEquipe                      |
|------|-----------------------------|
| ALM  |  AG2R La Mondiale           |
| AST  |  Astana Pro Team            |
| TBM  |  Bahrain - McLaren          |
| BOH  |  BORA - hansgrohe           |
| CCC  |  CCC Team                   |
| COF  |  Cofidis, Solutions Crédits |
| DQT  |  Deceuninck - Quick Step    |
| EF1  |  EF Pro Cycling             |
| GFC  |  Groupama - FDJ             |
| LTS  |  Lotto Soudal               |
| ...  | ...                         |




**relation Coureurs**

| dossard | nomCoureur  | prénomCoureur | codeEquipe |
|---------------|-------------|---------------|------------|
| 141           | LÓPEZ       | Miguel Ángel  | AST        |
| 142           | FRAILE      | Omar          | AST        |
| 143           | HOULE       | Hugo          | AST        |
| 11            | ROGLIČ      | Primož        | TJV        |
| 12            | BENNETT     | George        | TJV        |
| 41            | ALAPHILIPPE | Julian        | DQT        |
| 44            | CAVAGNA     | Rémi          | DQT        |
| 45            | DECLERCQ    | Tim           | DQT        |
| 121           | MARTIN      | Guillaume     | COF        |
| 122           | CONSONNI    | Simone        | COF        |
| 123           | EDET        | Nicolas       | COF        |
| …             | …           | …             | …          |





**relation Étapes**

| numéroEtape | villeDépart | villeArrivée      | km  |
|-------------|-------------|-------------------|-----|
| 1           | Nice        | Nice              | 156 |
| 2           | Nice        | Nice              | 185 |
| 3           | Nice        | Sisteron          | 198 |
| 4           | Sisteron    | Orcières-Merlette | 160 |
| 5           | Gap         | Privas            | 198 |
| ...         | ...         | ...               | ... |






**relation Temps**

| dossard | numéroEtape | tempsRéalisé |
|:-------------:|:-----------:|:------------:|
| 41            | 2           | 04:55:27     |
| 121           | 4           | 04:07:47     |
| 11            | 5           | 04:21:22     |
| 122           | 5           | 04:21:22     |
| ...           | ...         | ...          |



![](data/schema_tdf.png)

!!! example "Questions"
    === "Énoncé"
        1. Quel temps a réalisé Guillaume MARTIN sur l'étape Sisteron / Orcières-Merlette ?
        2. À l'arrivée à Privas, qui est arrivé en premier entre Primož ROGLIČ et Simone CONSONNI ?

    === "Correction"
        {{ correction(True,
        "
        
        "
        ) }}



