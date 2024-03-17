```python linenums='1'
def selection_enclos(animaux, num_enclos):
    table = []
    for animal in animaux:
        if animal['enclos'] == num_enclos:
            table.append(animal)
    return table
```