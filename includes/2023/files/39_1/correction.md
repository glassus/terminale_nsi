Version récursive :

```python linenums='1'
def fibonacci(n):
    if n == 1 :
        return 1   
    elif n == 1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
```

Version impérative :
```python linenums='1'
def fibonacci(n):
    a = 1
    b = 1
    for k in range(n-2):
        t = b
        b = a + b
        a = t
    return b

```



Version programmation dynamique :

```python linenums='1'
def fibonacci(n):
    d = {}
    d[1] = 1
    d[2] = 1
    for k in range(3, n+1):
        d[k] = d[k-1] + d[k-2]
    return d[n]
```

On peut constater que la version récursive échoue à calculer ```fibonacci(45)```, alors que les deux autres versions le font quasi-immédiatement. 

