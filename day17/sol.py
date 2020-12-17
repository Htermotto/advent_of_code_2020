# trash
from copy import deepcopy

lines = [l.strip() for l in open('input.txt', 'r')]


L = 20
W = 20
D = 13
H = 13

# 20X20X13X13 grid
hypergrid = []

# Create starting "hypergrid" record
grid = []
r = 6
blank = [['.'] * W for _ in range(L)]
for i in range(len(lines)):
    l = lines[i]
    c = 6
    for j in range(len(l)):
        blank[r][c] = l[j]
        c += 1
    r += 1
grid.append(blank)

for i in range(6):
    grid.append([['.'] * W for _ in range(L)])

for i in range(6):
    grid.insert(0, [['.'] * W for _ in range(L)])

hypergrid.append(grid)

# Create empty "hypergrid" records
for i in range(6):
    grid = []
    for i in range(D):
        grid.append([['.'] * W for _ in range(L)])
    hypergrid.append(grid)

for i in range(6):
    grid = []
    for i in range(D):
        grid.append([['.'] * W for _ in range(L)])
    hypergrid.insert(0, grid)


def get_neighbors(grid, x, y, z, w):
    num_active = 0
    num_inactive = 0
    for wd in range(-1, 2):
        for zd in range(-1, 2):
            for xd in range(-1, 2):
                for yd in range(-1, 2):
                    if wd == xd == yd == zd == 0:
                        continue

                    if x+xd < 0 or x+xd >= L or y+yd < 0 or y+yd>= W or z+zd <0 or z+zd >= D or w+wd < 0 or w+wd >= H:
                        continue

                    if grid[w+wd][z+zd][x+xd][y+yd] == '.':
                        num_inactive += 1
                    else:
                        num_active += 1
    return num_active, num_inactive

for i in range(6):
    next_grid = deepcopy(hypergrid)
    num_active = 0
    for w in range(H):
        for z in range(D):
            for x in range(L):
                for y in range(W):
                    active, inactive = get_neighbors(hypergrid, x, y, z, w)
                    if hypergrid[w][z][x][y] == '#':
                        if active == 2 or active == 3:
                            next_grid[w][z][x][y] = '#'
                            num_active += 1
                        else:
                            next_grid[w][z][x][y] = '.'
                    else:
                        if active == 3:
                            next_grid[w][z][x][y] = '#'
                            num_active += 1
                        else:
                            next_grid[w][z][x][y] = '.'
    hypergrid = next_grid

print(num_active)