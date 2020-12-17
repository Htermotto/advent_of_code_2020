# trash
from copy import deepcopy

lines = [l.strip() for l in open('input.txt', 'r')]


# 20X20X13X13 grid
hypergrid = []

# Create starting "hypergrid" record
grid = []
r = 6
blank = [['.'] * 20 for _ in range(20)]
for i in range(len(lines)):
    l = lines[i]
    c = 6
    for j in range(len(l)):
        blank[r][c] = l[j]
        c += 1
    r += 1
grid.append(blank)

for i in range(6):
    grid.append([['.'] * 20 for _ in range(20)])

for i in range(6):
    grid.insert(0, [['.'] * 20 for _ in range(20)])

hypergrid.append(grid)

# Create empty "hypergrid" records
for i in range(6):
    grid = []
    for i in range(13):
        grid.append([['.'] * 20 for _ in range(20)])
    hypergrid.append(grid)

for i in range(6):
    grid = []
    for i in range(13):
        grid.append([['.'] * 20 for _ in range(20)])
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

                    if x+xd < 0 or x+xd >=20 or y+yd < 0 or y+yd>=20 or z+zd <0 or z+zd >= 13 or w+wd < 0 or w+wd>=13:
                        continue

                    if grid[w+wd][z+zd][x+xd][y+yd] == '.':
                        num_inactive += 1
                    else:
                        num_active += 1
    return num_active, num_inactive

for i in range(6):
    next_grid = deepcopy(hypergrid)
    num_active = 0
    for w in range(13):
        for z in range(13):
            for x in range(20):
                for y in range(20):
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