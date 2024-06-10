### Exercice 1

**Partie A**

Liste des commandes UNIX à connaître :

- ```ls``` : donne la liste des fichiers et répertoires de l'emplacement courant
- ```cd``` : pour Change Directory, permet de changer de répertoire.
    - ```cd truc``` : va dans le répertoire ```truc``` (il faut que ```truc``` soit un repertoire de l'emplacement courant)
    - ```cd ..``` : remonte dans le répertoire parent de l'emplacement courant
- ```mv truc/ ailleurs/``` : déplace l'intégralité du dossier ```truc``` dans le dossier ```ailleurs```
- ```cp truc/ ailleurs/``` : copie l'intégralité du dossier ```truc``` dans le dossier ```ailleurs```


{{
correction(True,
"""
??? success \"Correction Q1\" 
    ```ls documents```
    ou
    ```
    cd documents
    ls
    ``` 
"""
)
}}


{{
correction(True,
"""
??? success \"Correction Q2\" 
    La totalité du dossier ```multimedia``` va être déplacée et sera maintenant un sous-dossier de ```documents```.
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q3\" 
    La classe  ```Arbre``` ne permet d'avoir que deux attributs ```gauche``` et ```droit``` alors que ```documents``` présente 3 sous-dossiers.
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q4\" 
    C'est un parcours préfixe. 
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q5\" 
    ```home-documents-multimedia-cours-administratif-personnel-images-videos-films``` 
"""
)
}}


**Partie B**


{{
correction(True,
"""
??? success \"Correction Q6\" 
    ```python linenums='1'
    def est_vide(self):
        return self.fils == []
    ```
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q7\" 
    ```python linenums='1'
    films = Dossier('films', [])
    videos = Dossier('videos', [films])
    images = Dossier('images', [])
    var_multimedia = Dossier('multimedia', [images, videos])
    ```
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q8\" 
    ```python linenums='1'
    def parcours(self):
        print(self.nom)
        for f in self.fils:
            f.parcours()
    ``` 
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q9\" 
    Sur une arborescence de fichiers, il arrive toujours un moment où un dossier ne contient plus de sous-dossiers. À ce moment là, l'appel récursif se fera donc uniquement sur des fichiers, dont l'attribut ```fils``` est une liste vide, qui ne déclenchera donc aucun appel. 
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q10\" 
    ```python linenums='1'
    def parcours(self):
        for f in self.fils:
            f.parcours()
        print(self.nom)
    ``` 
"""
)
}}

{{
correction(True,
"""
??? success \"Correction Q11\" 
    Un appel à la méthode ```parcours``` va afficher même le contenu des sous-dossiers, alors que ```ls``` ne le fait pas.
"""
)
}}

{{
correction(False,
"""
??? success \"Correction Q12\"
    ```python linenums='1'
    def mkdir(self, nom):
        new_doss = Dossier(nom, [])
        self.fils.append(new_doss)
    ```

"""
)
}}

{{
correction(False,
"""
??? success \"Correction Q13\" 
    ```python linenums='1'
    def contient(self, nom_dossier):
        if self.nom == nom_dossier:
            return True
        if self.fils == []:
            return False
        else:
            rep = False
            for f in self.fils:
                rep = rep or f.contient(nom_dossier)
            return rep    
    ```

    ou bien

    ```python linenums='1'
    def contient(self, nom_dossier):
        if self.nom == nom_dossier:
            return True
        if self.fils == []:
            return False
        else:
            return any([f.contient(nom_dossier) for f in self.fils])    
    ```
"""
)
}}

{{
correction(False,
"""
??? success \"Correction Q14\" 
    Il pourrait refaire un parcours infixe et observer si le dossier cherché est un fils du dossier actuel, et dans ce cas afficher le nom du dossier actuel.  
"""
)
}}

{{
correction(False,
"""
??? success \"Correction Q15\" 
    Il suffit de rajouter un attribut ```self.parent```. 
"""
)
}}