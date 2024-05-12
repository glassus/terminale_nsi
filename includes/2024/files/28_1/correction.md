Version récursive :

```python linenums='1'
def fibonacci(n):
    if n <= 2 :
        return n   
    else :
        return fibonacci(n-1) + fibonacci(n-2)
```




Version programmation dynamique bottom-up:

```python linenums='1'
def fibonacci(n):
    d = {}
    d[1] = 1
    d[2] = 1
    for k in range(3, n+1):
        d[k] = d[k-1] + d[k-2]
    return d[n]
```


Version programmation dynamique top-down avec mémoïsation:

```python linenums='1'
dict_fibo = {1:1, 2:1}
def fibonacci(n):
    if n in dict_fibo:
        return dict_fibo[n]
    dict_fibo[n] = fibonacci(n-1) + fibonacci(n-2)
    return dict_fibo[n]
```








On peut constater que la version récursive échoue à calculer ```fibonacci(45)```, alors que les deux autres versions le font quasi-immédiatement. 

