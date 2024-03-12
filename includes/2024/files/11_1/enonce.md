Pour cet exercice :

- On appelle « mot » une chaîne de caractères composée avec des caractères choisis
parmi les 26 lettres minuscules ou majuscules de l'alphabet,

- On appelle « phrase » une chaîne de caractères :
    - composée avec un ou plusieurs « mots » séparés entre eux par un seul
caractère espace `' '`,
    - se finissant :
        - soit par un point `'.'` qui est alors collé au dernier mot,
        - soit par un point d'exclamation `'!'` ou d'interrogation `'?'` qui est alors
séparé du dernier mot par un seul caractère espace `' '`.

*Exemples :*

- 'Cet exercice est simple.'
- 'Le point d exclamation est separe !'

Après avoir remarqué le lien entre le nombre de mots et le nombres de caractères espace
dans une phrase, programmer une fonction `nombre_de_mots` qui prend en paramètre une
phrase et renvoie le nombre de mots présents dans cette phrase.

```python
>>> nombre_de_mots('Le point d exclamation est separe !')
6
>>> nombre_de_mots('Il y a un seul espace entre les mots !')
9
>>> nombre_de_mots('Combien de mots y a t il dans cette phrase ?')
10
>>> nombre_de_mots('Fin.')
1
```

