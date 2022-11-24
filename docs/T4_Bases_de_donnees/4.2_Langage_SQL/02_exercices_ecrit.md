# Exercices SQL débranchés

{{initexo(0)}}



!!! abstract "{{ exercice() }}"

    *(d'après Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.)*

    On veut créer une base de données ```baseHopital.db```  qui contiendra les trois tables suivantes :

    |  | Patients |
    |-----|----|
    | id | ```Int```  |
    | nom | ```Text```  |
    | prenom | ```Text```  |
    | genre | ```Text```  |
    | annee_naissance | ```Int```  |


    |  | Ordonnances |
    |-----|----|
    | code | ```Int```  |
    | id_patient | ```Int```  |
    | matricule_medecin  | ```Int```  |
    | date_ord | ```Text```  |
    | medicaments | ```Text```  |

    |  | Medecins |
    |-----|----|
    | matricule | ```Int```  |
    | nom_prenom | ```Text```  |
    | specialite | ```Text```  |
    | telephone | ```Text```  |


    On suppose que les dates sont données sous la forme ```jj-mm-aaaa```.

    On donne le diagramme relationnel de cette base :
    ![image](data/deb_ex1.png){: .center}
    
    **Q0.** Écrire le schéma relationnel de la table Ordonnances. On soulignera les clés primaires et marquera d'un # les clés étrangères.

    ??? note "Correction"
        Ordonnaces ((<ins>code</ins>, Int), (id_patient#, Int), (matricule_medecin#, Int), (date_ord, Text), (medicaments, Text))


    **Q1.** (HP) Donner les commandes SQL permettant de créer ces tables.

    ??? note "Correction"
        ```SQL
        CREATE TABLE Patients(
        id INTEGER PRIMARY KEY,
        nom TEXT,
        prenom TEXT,
        genre TEXT,
        annee_naissance INTEGER
        );

        CREATE TABLE Ordonnances(
        code INTEGER PRIMARY KEY,
        id_patient INTEGER,
        matricule_medecin INTEGER,
        date_ord TEXT,
        medicaments TEXT,
        FOREIGN KEY(id_patient) REFERENCES Patients(Id),
        FOREIGN KEY(matricule_medecin) REFERENCES Medecins(matricule)
        );

        CREATE TABLE Medecins(
        matricule INTEGER  PRIMARY KEY,
        nom_prenom TEXT,
        specialite TEXT,
        telephone TEXT
        );

        ```



    **Q2.** Mme Anne Wizeunid, née en 2000 et demeurant 3 rue des Pignons Verts 12345 Avonelit doit être enregistrée comme patiente numéro 1. Donner la commande SQLite correspondante.

    ??? note "Correction"
        ```SQL
        INSERT INTO Patients VALUES (1, "Wizeunit", "Anne", "F", 2000);
        ```
     

      **Q3.** Le patient numéro 100 a changé de prénom et s'appelle maintenant "Alice". Donner la commande SQLite modifiant en conséquence ses données.

    ??? note "Correction"
        ```SQL
        UPDATE Patients SET prenom = 'Alice' WHERE id = 100 ;
        ```


      **Q4.** Par souci d'économie, la direction décide de se passer des médecins spécialisés en épidémiologie. Donner la commande permettant de supprimer leurs fiches.


    ??? note "Correction"
        ```SQL
        DELETE FROM Medecins WHERE specialite = "épidémiologie";
        ```

    **Q5.**  Donner la liste des patient(e)s ayant été examiné(e)s par un(e) psychiatre en avril 2020.
      
    ??? note "Correction"
        ```SQL
        SELECT p.nom, p.prenom FROM Patients AS p
        JOIN Ordonnances AS o ON p.id = o.id_patient
        JOIN Medecins AS m ON o.matricule_medecin = m.matricule
        WHERE m.specialite = "psychiatrie" AND o.date_ord LIKE "%04-2020%"

        ```


!!! abstract "{{exercice()}}"
    _basé sur le travail de G.Viateau (Bayonne)_

    On considère ci-dessous le schéma de la base de données du stock d'un supermarché :

    ![](data/exo3_schema.png)

    **Q1**. Quelle requête SQL donne le prix d'achat du produit dont le ```nom_court``` est «Liq_Vaiss_1L» ?
{#
    ??? note "Correction"
        ```SQL
        SELECT prix_achat FROM Produits WHERE nom_court = 'Liq_Vaiss_1L' 
        ```
#}

    **Q2**. Quelle requête donne l'adresse, le code postal et la ville du fournisseur dont le nom est «Avenir_confiseur» ?

{# 
    ??? note "Correction"
        ```SQL
        SELECT adresse, cp, ville FROM Fournisseurs WHERE nom = 'Avenir_confiseur';
        ``` 
#}



    **Q3**. Quelle requête donne les produits étant en rupture de stock ?
{#
    ??? note "Correction"
        ```SQL
        SELECT Produits.nom FROM Produits
        JOIN Stocks ON Produits.id = Stocks.produit
        WHERE Stocks.quantite = 0;
        ```
#}

    **Q4**. Quelle requête donne la liste de toutes les ampoules vendues en magasin ? On pourra faire l'hypothèse que le nom du produit contient le mot «ampoule»
{#
    ??? note "Correction"
        ```SQL
        SELECT nom FROM Produits WHERE nom LIKE "%ampoule%";
        ```
#}

    **Q5**. Quelle requête permet d'avoir le prix moyen de ces ampoules ?
{#
    ??? note "Correction"
        ```SQL
        SELECT AVG(prix_vente) FROM Produits WHERE nom LIKE "%ampoule%";
        ```
#}

    **Q6**. Quelle requête permet d'identifier le produit le plus cher du magasin ?
{#
    ??? note "Correction"
        ```SQL
        SELECT nom_court FROM Produits ORDER BY prix_vente DESC LIMIT 1;
        ```
        ou

        ```SQL
        SELECT nom FROM Produits WHERE prix_vente = (SELECT MAX(prix_vente) FROM Produits);
        ``` 
#}

    **Q7**. Quelle requête renvoie les noms des produits dont la date de péremption est dépassée ? _(on pourra utiliser la fonction SQL ```NOW()``` qui renvoie la date actuelle )_
{#
    ??? note "Correction"
        ```SQL
        SELECT p.nom FROM Produits AS p
        JOIN Stocks AS s ON s.produits = p.id
        WHERE s.date_peremption < NOW();
        ```
#}

!!! abstract "{{exercice()}}"
    Exercice 1 du sujet [Amérique du Sud J1 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Amerique_Nord_J1.pdf){. target="_blank"}

    ??? note "Correction Q1.a."
        La relation Sport a pour clé primaire l'attribut NomSport et pour clé étrangère l'attribut nomStation, clé primaire de la relation Station.

    ??? note "Correction Q1.b."
        - Contrainte d'intégrité de domaine :  l'attribut Prix doit être un nombre entier.

        - Contrainte d'intégrité de relation :  le couple (nomSport, nomStation) ne peut pas se retrouver deux fois dans la table (car il forme une clé primaire)

        - Contrainte d'intégrité de référence :  l'attribut nomStation ne peut pas être un nom n'apparaissant pas dans la relation Station.

    ??? note "Correction Q2.a."
        La commande INSERT ne sert que pour insérer de nouveaux enregistrements, or le couple ("planche à voile" , "La tramontane catalane") existe déjà dans la relation (et c'est une clé primaire donc on ne peut pas la retrouver deux fois).
        Il faut donc utiliser :
        ```SQL
        UPDATE Sports SET prix = 1350 
        WHERE nomSport = "planche à voile" AND nomStation = "La tramontane catalane"        
        ```

    ??? note "Correction Q2.b."
        ```SQL
        INSERT INTO Station VALUES ("Soleil Rouge", "Bastia", "Corse")  
        INSERT INTO Sport VALUES ("plongée", "Soleil Rouge", 900)        
        ```

    ??? note "Correction Q3.a."
        ```SQL
        SELECT mail FROM Client        
        ```

    ??? note "Correction Q3.b."
        ```SQL
        SELECT nomStation FROM Sport
        WHERE nomSport = "plongee"      
        ```

    ??? note "Correction Q4.a."
        ```SQL
        SELECT Station.ville, Station.nomStation FROM Station
        JOIN Sport ON Sport.nomStation = Station.nomStation
        WHERE Sport.nomSport = "plongee"        
        ```

    ??? note "Correction Q4.b."
        ```SQL
        SELECT COUNT(*) FROM Sejour
        JOIN Station ON Station.nomStation = Sejour.nomStation
        WHERE Sejour.annee = 2020 AND Station.region = "Corse"
        ```




!!! abstract "{{exercice()}}"
    Exercice 4 du sujet [Centres Étrangers J1 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Centres_Etrangers_J1.pdf){. target="_blank"}

!!! abstract "{{exercice()}}"
    Exercice 4 du sujet [Métropole J2 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Metropole_J2.pdf){. target="_blank"}