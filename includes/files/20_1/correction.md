*Correction proposée par Yves Laurent*

```python


def xor(tab1, tab2):
    """

    Parameters
    ----------
    tab1 : type(tab1) = list
        Binaire 1
    tab2 : type(tab1) = list
        Binaire 2

    Returns
    -------
    resultat : list
        tab1 xor tab2.

    """
    assert len(tab1) == len(tab2), "pas la même taille"
    
    resultat = []
    
    taille = len(tab1)
    
    for compteur in range(taille):
        resultat.append(tab1[compteur]^tab2[compteur])
    
    return resultat

```