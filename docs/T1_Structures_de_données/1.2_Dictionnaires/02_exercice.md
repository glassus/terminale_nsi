# Création d'une rainbow table

**Objectif** :

Créer une fonction ```inverse_md5()``` qui va chercher dans un dictionnaire (construit préalablement) la clé éventuelle correspondant au hash donné en paramètre.

Exemple : 
```
>>> inverse_md5(0571749e2ac330a7455809c6b0e7af90)
>>> 'sunshine'
```


**Aide :**

- liste de 1000 mots de passe fréquents : [ici](http://glassus1.free.fr/extraitrockyou.txt)
- comment lire / convertir le contenu d'un fichier : [ici](https://github.com/glassus/nsi/blob/master/Premiere/Theme07_Interactions_Homme_Machine_Web/03_Get_Post_Formulaires.md#pr%C3%A9-requis-2--lextraction-dun-fichier-texte-sous-forme-de-liste)
- comment calculer du MD5 en python : librairie [hashlib](https://www.geeksforgeeks.org/md5-hash-python/)
(vérifiez bien que "vive la NSI" donne bien e74fb2f94c052bbf16cea4a795145e35)