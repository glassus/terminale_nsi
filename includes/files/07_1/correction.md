```python linenums='1'
def conv_bin(n):
    b = []
    bits = 0
    while n != 0:
        b.append(n % 2)
        bits += 1
        n = n // 2
    b.reverse()
    return (b, bits)

```