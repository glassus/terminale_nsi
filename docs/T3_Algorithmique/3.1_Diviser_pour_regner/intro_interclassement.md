# Vers l'algorithme d'interclassement


!!! tip "Principe de l'interclassement"
    Pour interclasser deux listes ```lst1``` et ```lst2```.

    - on part d'une liste vide ```lst_totale```
    - on y ajoute alternativement les éléments de ```lst1``` et ```lst2```, en veillant à maintenir un ordre croissant. Il faut pour cela gérer séparément un indice ```i1``` pour la liste ```lst1```  et un indice ```i2```  pour la liste ```i2```.
    - quand une liste est épuisée, on y ajoute la totalité restante de l'autre liste.



Exemple d'utilisation :

```python
>>> interclassement([2, 4, 5, 13, 15, 19], [3, 7, 8, 10, 16])
[2, 3, 4, 5, 7, 8, 10, 13, 15, 16, 19]
```


??? note "Code à trous :star: :star: :star: :star:"
    ```python linenums='1'
    def interclassement(lst1, lst2):
        ...
                           
    ``` 


??? note "Code à trous :star: :star: :star: :octicons-star-24: " 
    ```python linenums='1'
    def interclassement(lst1, lst2):
        i1 = ...
        i2 = ...
        lst_totale = ...
        while ...:
            if ...:
                lst_totale.append(...)
                ...
            else:
                lst_totale.append(...)
                ...
        return ... + ... + ...                        
    ``` 

??? note "Code à trous :star: :star: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def interclassement(lst1, lst2):
        i1 = ...
        i2 = ...
        lst_totale = ...
        while i1 !=... and i2 != ...:
            if ... < ...:
                lst_totale.append(...)
                ... += ...
            else:
                lst_totale.append(...)
                ... += ...
        return ... + ... + ...                           
    ``` 



??? note "Code à trous :star: :octicons-star-24: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def interclassement(lst1, lst2):
        i1 = ...
        i2 = ...
        lst_totale = ...
        while i1 != len(...) and i2 != len(...):
            if lst1[...] < lst2[...]:
                lst_totale.append(...)
                ... += 1
            else:
                lst_totale.append(lst2[...])
                ... += 1
        return lst_totale + lst1[...] + lst2[...]                      
    ``` 
        