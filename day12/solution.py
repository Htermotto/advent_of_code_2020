lines = [l.strip() for l in open('input.txt', 'r')]

position = (0,0)
waypoint = (10, 1)

east = (1,0)
west = (-1,0)
north = (0,1)
south = (0,-1)

dirs = [north, east, south, west]

curr_dir = east
facing = east
for move in lines:
    d = move[0]
    amt = int(move[1:])
    if d == 'N':
        curr_dir = north
    elif d == 'E':
        curr_dir = east
    elif d == 'S':
        curr_dir = south
    elif d == 'W':
        curr_dir = west
    elif d == 'L':
        turns = amt // 90
        for i in range(turns):
            waypoint = (-waypoint[1], waypoint[0])
        # curr_index = dirs.index(facing)
        # facing = dirs[(curr_index + turns) % 4]
        continue
    elif d == 'R':
        turns = amt // 90
        for i in range(turns):
            waypoint = (waypoint[1], -waypoint[0])
        # curr_index = dirs.index(facing)
        # facing = dirs[(curr_index - turns) % 4]
        continue
    elif d == 'F':
        position = (position[0] + (amt * waypoint[0]), position[1] + (amt * waypoint[1]))
        continue

    waypoint = (waypoint[0] + (amt * curr_dir[0]), waypoint[1] + (amt * curr_dir[1]))

    print(position)
    print(waypoint)
    print('\n')

print(position)
print(abs(position[0]) + abs(position[1]))