# Vers l'algorithme de dichotomie

Exemple d'utilisation :

```python
>>> tab = [1, 5, 7, 9, 12, 13]
>>> recherche_dichotomique(tab, 12)
True
>>> recherche_dichotomique(tab, 17)
False
```


??? note "Code à trous, newbie version"
    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        i_debut = ...
        i_fin = ...
        while ... <= ... :
            i_centre = (... + ...) // 2     
            val_centrale = tab[...]         
            if val_centrale == val:              
                return ...
            if val_centrale < val:                
                i_debut = ... + 1            
            else :
                i_fin = ... - 1
        return False
    ```


??? note "Code à trous, regular version"
    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        i_debut = ...
        i_fin = ...
        while ... <= ... :
            i_centre = ...   
            val_centrale = ...         
            if ... == ... :              
                return ...
            if ... < ...:                
                i_debut = ...        
            else :
                i_fin = ...
        return False
    ```

??? note "Code à trous, expert version"
    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        ... = ...
        ... = ...
        while ... <= ... :
            ... = ...   
            ... = ...         
            if ... == ... :              
                return ...
            if ... < ...:                
                ... = ...         
            else :
                ... = ...
        return False
    ```


??? note "Code à trous, God version"
    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        ...
    ```

Pour tester :

```python
>>> tab = [1, 5, 7, 9, 12, 13]
>>> recherche_dichotomique(tab, 12)
True
>>> recherche_dichotomique(tab, 17)
False
```