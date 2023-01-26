```python linenums='1'
def a_doublon(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False
```