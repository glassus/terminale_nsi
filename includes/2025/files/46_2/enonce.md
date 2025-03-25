On considère dans cet exercice un algorithme glouton pour le rendu de monnaie. Pour
rendre une somme en monnaie, on utilise à chaque fois la plus grosse pièce possible et ainsi
de suite jusqu’à ce que la somme restante à rendre soit nulle.

Les pièces de monnaie utilisées sont :

`pieces = [1, 2, 5, 10, 20, 50, 100, 200]`

On souhaite écrire une fonction `rendu_monnaie` qui prend en paramètres

- un entier `somme_due` représentant la somme à payer ;
- un entier `somme_versee` représentant la somme versée qui est supérieure ou égale
à `somme_due` ;

et qui renvoie un tableau de type `list` contenant les pièces qui composent le rendu
de la monnaie restante, c’est-à-dire de `somme_versee - somme_due`.



Ainsi, l’instruction `rendu_monnaie(452, 500)` renvoie le tableau `[20, 20, 5, 2, 1]`.

En effet, la somme à rendre est de `48` euros soit `20 + 20 + 5 + 2 + 1`.

Le code de la fonction `rendu_monnaie` est donné ci-dessous :

```python linenums='1'
def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = ... 
    a_rendre = ... 
    i = len(pieces) - 1
    while a_rendre > ...: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(...) 
        a_rendre = ... 
    return rendu

```

Compléter ce code et le tester :

```python
>>> rendu_monnaie(700, 700)
[]
>>> rendu_monnaie(102, 500)
[200, 100, 50, 20, 20, 5, 2, 1]
```