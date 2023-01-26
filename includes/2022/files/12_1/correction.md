L'énoncé n'est pas très clair quand il dit «d'afficher 'erreur'» (ce qui suppose un `print` et non un `return`). Nous choississons donc dans ce cas de renvoyer ```None```.

```python linenums='1'
def moyenne(tab):
    if tab == []:
        print('erreur')
        return None
    else:
        somme = 0
        for elt in tab:
            somme += elt
        return somme / len(tab)

```