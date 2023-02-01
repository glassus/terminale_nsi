# Exercice : création d'une rainbow table :rainbow:

**Objectif** :

Créer une fonction ```inverse_md5()``` qui va chercher dans un dictionnaire (construit préalablement) le mot correspondant au hash donné en paramètre.

Exemple : 
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