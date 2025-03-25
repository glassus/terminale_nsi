```python linenums='1' hl_lines='3 4 6 10 13 18 19'
def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0: 
        return str(r) 
    else:
        return dec_to_bin(q) + str(r) 

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0': 
            return 0
        else:
            return 1 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit
```