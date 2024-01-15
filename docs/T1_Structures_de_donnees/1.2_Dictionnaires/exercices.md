# Exercices sur les dictionnaires

{{initexo(0)}}



!!! abstract "{{ exercice() }} : création d'une rainbow table :rainbow:"
    Créer une fonction ```inverse_md5()``` qui va chercher dans un dictionnaire (construit préalablement) le mot correspondant au hash donné en paramètre.

    À quel mot de passe correspond le hash ```33da7a40473c1637f1a2e142f4925194``` ?

    **Exemple :** 
    ```
    >>> inverse_md5('0571749e2ac330a7455809c6b0e7af90')
    >>> 'sunshine'
    ```


    **Aide :**

    - liste de 1000 mots de passe fréquents : [ici](http://glassus1.free.fr/extraitrockyou.txt)
    - comment lire / convertir le contenu d'un fichier dans une liste de ```string``` :
    ```python
    lst = open("monfichier.txt").read().splitlines()
    ```
    - comment calculer du MD5 en Python : 
    ```python
    import hashlib
    result = hashlib.md5('azerty'.encode())
    print(result.hexdigest())
    ```

    {{
    correction(False,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        import hashlib

        lst = open('extraitrockyou.txt').read().splitlines()
        inv_hash = {}
        for mdp in lst:
            hsh = hashlib.md5(mdp.encode()).hexdigest()
            inv_hash[hsh] = mdp


        def inverse_md5(hsh):
            return inv_hash[hsh]
        ```
    """
    )
    }}

!!! abstract "{{ exercice() }}"
    Exercice 2 du sujet [Centres Etrangers J1 2021](https://glassus.github.io/terminale_nsi/T6_Annales/data/2021/21_Centres_Etrangers_1.pdf){. target="_blank"}

    {{
    correction(True,
    """
    ??? success \"Correction Q1.a. \" 
        ```flotte[26]``` renvoie  ```{'type' : 'classique', 'etat' : 1, 'station' : 'Coliseum'}```
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q1.b. \" 
        ```flotte[80]['etat']``` renvoie la valeur ```0```. 
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q1.c. \" 
        ```flotte[99]['etat']``` renverra une erreur car la clé 99 n'existe pas. 
    """
    )
    }}


    {{
    correction(True,
    """
    ??? success \"Correction Q2.a. \" 
        Les valeurs possibles pour ```choix``` sont ```electrique``` ou ```classique```. 
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q2.b. \" 
        En fonction du choix (```electrique``` ou ```classique```), cette fonction va renvoyer le nom de la première station où un vélo est disponible (à l'```etat``` 1).  
        Seule la première station sera renvoyée, à cause du ```return```. Si aucun vélo n'est disponible, la fonction ne renverra rien. 
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q3.a. \" 
        ```python linenums='1'
        for id_velo in flotte:
            if flotte[id_velo]['station'] == 'Citadelle' and flotte[id_velo]['etat'] == 1:
                print(id_velo)
        ``` 
    """
    )
    }}


    {{
    correction(True,
    """
    ??? success \"Correction Q3.b. \" 
        ```python linenums='1'
        for id_velo in flotte:
            if flotte[id_velo]['type'] == 'electrique' and flotte[id_velo]['etat'] != -1:
                print(id_velo, flotte[id_velo]['station'])
        ``` 
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q4. \" 
        ```python linenums='1'
        def velo_finder(coordonnees):
            velo_dispo = []
            for id_velo in flotte:
                d = distance(coordonnees, stations[flotte[id_velo]['station']])
                if d < 800 and flotte[id_velo]['etat'] == 1:
                    velo_dispo.append((flotte[id_velo]['station'], d, id_velo))
            return velo_dispo
        ```        
    """
    )
    }}


     
    