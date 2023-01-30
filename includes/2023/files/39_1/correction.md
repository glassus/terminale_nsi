Version récursive :

```python linenums='1'
def fibonacci(n):
    if n == 0 :
        return 0   
    elif n == 1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
```

Version impérative :
```python linenums='1'
def fibonacci(n):
    a = 0
    b = 1
    for k in range(n-1):
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

