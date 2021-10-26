# Algorithmes de référence :heart:

## 1. Factorielle récursive


```python linenums='1'
def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n - 1)
```

## 2. PGCD récursif

```python linenums='1'
def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a%b)
```

## 3. Puissance récursive (simple)
```python linenums='1'
def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n-1)
```

## 4. Puissance récursive (optimisée)
```python linenums='1'
def puissance(x, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return puissance(x*x, n//2)
        else :
            return x*puissance(x*x, (n-1)//2)
```

## 5. Recherche dichotomique récursive (avec slicing)
*Note : le slicing de liste n'est pas au programme de NSI.*

```python linenums='1'
def recherche(lst, m):
    if len(lst) == 1: 
        if lst[0] == m:
            return True
        else :
            return False
    else:              
        mid = len(lst)//2
        if lst[mid] > m:
            return recherche(lst[:mid], m)
        else :
            return recherche(lst[mid:], m)
```