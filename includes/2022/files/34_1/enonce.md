Écrire une fonction `occurrence_max` prenant en paramètres une chaîne de caractères
`chaine` et qui renvoie le caractère le plus fréquent de la chaîne. La chaine ne contient
que des lettres en minuscules sans accent.
On pourra s’aider du tableau

`alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']`

et du tableau `occurrence` de 26 éléments où l’on mettra dans `occurrence[i]` le
nombre d’apparitions de `alphabet[i]` dans la chaine.  
Puis on calculera l’indice `k` d’un maximum du tableau `occurrence` et on affichera `alphabet[k]`.

Exemple :
```python
>>> ch = 'je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
>>> occurrence_max(ch)
‘e’
```