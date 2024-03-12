```python linenums='1'
def selection_enclos(table_animaux, num_enclos):
    table = []
    for animal in table_animaux:
        if animal['enclos'] == num_enclos:
            table.append(animal)
    return table
```