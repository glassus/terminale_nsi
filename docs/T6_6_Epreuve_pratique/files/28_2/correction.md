```python linenums='1'
def dec_to_bin(a):
    bin_a = ''
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a
```