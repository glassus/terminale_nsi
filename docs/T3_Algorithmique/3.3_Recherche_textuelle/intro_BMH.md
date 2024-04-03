# Vers Boyer-Moore-Horspool

L'idée est d'améliorer le code précédent (celui on parcourt le motif à l'envers) en **sautant** directement au prochain endroit potentiellement valide. 

Pour cela on regarde le caractère ```X```  du texte sur lequel on s'est arrêté (car ```X``` n'était pas égal au caractère de rang équivalent dans le motif):

- si ```X``` n'est pas dans le motif, il est inutile de se déplacer "de 1" : on retomberait tout de suite sur ```X```, c'est du temps perdu. On se décale donc juste assez pour dépasser ```X```, donc de la longueur du motif cherché.
- si ```X``` est dans le motif (sauf à la dernière place du motif !), on va regarder la place de la dernière occurence de ```X``` dans le motif et de déplacer de ce nombre, afin de faire coïncider le ```X``` du motif et le ```X``` du texte.

???+ tip "Illustration de l'algorithme"
    <gif-player src="https://glassus.github.io/terminale_nsi/T3_Algorithmique/3.3_Recherche_textuelle/data/gif_BM.gif" speed="1" play></gif-player>

    _Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._


On dispose de la fonction ```dico_lettres``` :
```python linenums='1'
def dico_lettres(mot):
    d = {}
    for i in range(len(mot)-1):
        d[mot[i]] = i
    return d
```

*Exemple d'utilisation de la fonction ```BMH``` :*

```python
>>> BMH("une magnifique maison bleue", "maison")
[15]
>>> BMH("une magnifique maison bleue", "nsi")
[]
>>> BMH("une magnifique maison bleue", "ma")
[4, 15]
```




??? note "Code à trous :star: :star: :star: :star:"
    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):


    ```


??? note "Code à trous :star: :star: :star: :octicons-star-24: " 
    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):
        dico = dico_lettres(motif)
        indices = ...
        i = ...
        while i < ...:
            ...
            while k < ...
                ...
            if k == ...
                ...
                ...
            else:
                if ...
                    ...
                else:
                    ...

        return ...

    ```

??? note "Code à trous :star: :star: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):
        dico = dico_lettres(motif)
        indices = ...
        i = len(...) -1
        while i < len(...):
            k = 0
            while k < ... and motif[...] == texte[...]:
                k += ...
            if k ==...
                indices.append(...)
                i += ...
            else:
                if ... in dico: 
                    i = ...
                else:
                    i = ...

        return ...

    ```



??? note "Code à trous :star: :octicons-star-24: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):
        dico = dico_lettres(...)
        indices = []
        i = len(...) -1
        while i < len(...):
            k = 0
            while k < len(...) and motif[...] == texte[...]: #(1)
                k += ...
            if k == len(...):
                indices.append(...)
                i += ...
            else:
                if texte[...] in dico: (#4)
                    i = max(i - k  + len(...) - dico[texte[...]] - 1, i+1) 
                else:
                    i = i - k + len(...) #(6)

        return ...

    ```
        



