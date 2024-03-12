Le codage par différence (*delta encoding* en anglais) permet de compresser un tableau de
données en indiquant pour chaque donnée, sa différence avec la précédente (plutôt que la
donnée elle-même). On se retrouve alors avec un tableau de données plus petit, nécessitant
moins de place en mémoire. Cette méthode se révèle efficace lorsque les valeurs consécutives
sont proches. 

Programmer la fonction `delta(liste)` qui prend en paramètre un tableau non vide de nombres entiers
et qui renvoie un tableau contenant les valeurs entières compressées à l’aide cette technique.


Exemples :

```python
>>> delta([1000, 800, 802, 1000, 1003])
[1000, -200, 2, 198, 3]
>>> delta([42])
[42] 
```

