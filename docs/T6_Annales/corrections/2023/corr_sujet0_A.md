# Correction du sujet 0 version A / 2023

:arrow_right: [Sujet](../../data/2023/2023-sujet_0-a.pdf){. target="_blank"}

## Exercice 1

??? tip "correction Q1."
    Les attributs de la table ```groupes``` sont ```idgrp```, ```nom```, ```style``` et ```nb_pers```.

??? tip "Correction Q2."
    Le musicien Charlie Parker est présent 2 fois dans cette table (avec deux instruments différents). L'attribut ```nom``` ne peut donc pas être une clé primaire, qui doit être unique.

??? tip "Correction Q3."
    Cette requête renvoie ```'Weather Report'``` et ```'Return to Forever'```.

??? tip "Correction Q4."
    ```sql
    UPDATE concerts
    SET heure_fin = '22h30'
    WHERE idconc = 36;
    ```

??? tip "Correction Q5."
    ```sql
    SELECT groupes.nom
    FROM groupes
    JOIN concerts ON concerts.idgrp = groupes.idgrp
    WHERE concerts.scene = 1;
    ```
    
??? tip "Correction Q6."
    ```sql
    INSERT INTO groupes
    VALUES (15, 'Smooth Jazz Fourplay', 'Free Jazz', 4);
    ```
??? tip "Correction Q7."
    ```python linenums='1'
    def recherche_nom(tab_mus):
        lst = []
        for mus in tab_mus:
            if mus['nb_concerts'] >= 4:
                lst.append(mus['nom'])
        return lst
    ```

## Exercice 2

??? tip "correction Q1."
    Cet ordinateur appartient à Alice car il fait partie du réseau ```172.16.2.0/24```. Le masque en ```/24``` nous indique que ce réseau contiendra des adresses de type ```172.16.2.X```, ce qui est bien le cas de l'adresse ```172.16.2.3```.

??? tip "Correction Q2."
    $C=\dfrac{10000}{1000}=10$.

??? tip "Correction Q3."
    Table de routage du routeur `R6`

    |Destination|Pass|Coût|
    |:--:|:--:|:--:|
    |LAN1|R5|21|
    |LAN2|-|-|
    |WAN1|R5|11|
    |WAN2|R5|20|
    |WAN3|R5|11|
    |WAN4|R5|12|
    |WAN5|R5|10|
    |WAN6|-|-|
    |WAN7|-|-|
    |WAN8|R5|10|

??? tip "Correction Q4."
    ```R1-R2-R5-R6``` 
    
??? tip "Correction Q5."
    Le nouveau coût de 111 correspond à la route ```R1-R2-R4-R6```. Ce sera la nouvelle route la plus courte si le routeur `R5` tombe en panne. 
     
    
    
