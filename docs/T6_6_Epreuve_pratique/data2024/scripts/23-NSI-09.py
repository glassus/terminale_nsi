# -*- coding: utf-8 -*-

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // ...
    if ... < n:
        return chercher(tab, n, ..., ...)
    elif ... > n:
        return chercher(tab, n, ..., ...)
    else:
        return ...