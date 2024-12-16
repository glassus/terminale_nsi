data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

import networkx as nx

def make_grid(data):
    d = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            d[x+y*1j] = data[y][x]
            if data[y][x] == 'S':
                start = x+y*1j
            if data[y][x] == 'E':
                end = x+y*1j
    return d, start, end

def voisins(grid, pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if npos in grid and grid[npos] in '.SE':
            lst.append(npos)
    return lst

grid, start, end = make_grid(data)

G = nx.Graph()
for pos in grid:
    if grid[pos] != '#':
        vois = voisins(grid, pos)
        for v in vois:
            G.add_edge(pos, v)
            

def are_col(a, b, c):
    u = (b.real-a.real, b.imag-a.imag)
    v = (c.real-b.real, c.imag-b.imag)
    
    return u[0]*v[1] == u[1]*v[0]


def score(lst):
    n = len(lst)
    s = 0
    if not are_col(start-1, lst[0], lst[1]):
        s += 1001
    else:
        s += 1
    for i in range(1, n-1):
        if not are_col(lst[i-1], lst[i], lst[i+1]):
            s += 1001
        else:
            s += 1
    return s

seen = set()
chemins = nx.all_simple_paths(G, source=start, target=end)
M = 10**12
for ch in chemins:
    m = score(ch)
    if m == 78428:
        for p in ch:            
            seen.add(p)
print(len(seen))

