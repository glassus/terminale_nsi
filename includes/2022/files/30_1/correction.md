```python linenums='1'
def fusion(tab1, tab2):
    tab_fusion = []
    i1 = 0
    i2 = 0
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_fusion.append(tab1[i1])
            i1 += 1
        else:
            tab_fusion.append(tab2[i2])
            i2 += 1
            
    if i1 == len(tab1):
        while i2 < len(tab2):
            tab_fusion.append(tab2[i2])
            i2 += 1
    else:
        while i1 < len(tab1):
            tab_fusion.append(tab1[i1])
            i1 += 1        
            
    return tab_fusion
```