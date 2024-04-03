# Vers la recherche textuelle naïve

!!! tip "Illustration de l'algorithme"
    <gif-player src="https://glassus.github.io/terminale_nsi/T3_Algorithmique/3.3_Recherche_textuelle/data/gif_naive.gif" speed="1" play></gif-player>


Écrire une fonction ```recherche_naive``` qui prend en paramètres deux chaines de caractères ```texte``` et ```motif``` et qui renvoie la liste des indices (éventuellement vide) des occurrences de la chaîne `motif` dans la chaîne `texte`.


Exemple d'utilisation :
```python
>>> recherche_naive("une magnifique maison bleue", "maison")
[15]
>>> recherche_naive("une magnifique maison bleue", "nsi")
[]
>>> recherche_naive("une magnifique maison bleue", "ma")
[4, 15]
```


??? note "Code à trous :star: :star: :star: :star:"
    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''


                           
    ``` 


??? note "Code à trous :star: :star: :star: :octicons-star-24: " 
    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        indices = ...
        i = ...
        while ...:
            ...
            while ...:
                ...
            if ...:
                ...
            ...

        return ...
                         
    ``` 

??? note "Code à trous :star: :star: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        indices = ...
        i = ...
        while i <= ...:
            k = ...
            while k < ... and ...:
                ...
            if ...:
                indices.append(...)
            i += ...

        return ...
                           
    ``` 



??? note "Code à trous :star: :octicons-star-24: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        indices = []
        i = 0
        while i <= ... - ...:
            k = ...
            while k < len(...) and texte[...] == motif[...]:
                k += ...
            if k == len(...):
                indices.append(...)
            i += ...

        return ...
                            
    ``` 
        



