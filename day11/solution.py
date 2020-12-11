lines = [list(l.strip()) for l in open('input.txt', 'r')]


def num_occupied(matrix, r, c):
    num_occupied = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if r+i >= len(matrix) or c+j >= len(matrix[0]) or r+i < 0 or c+j < 0:
                continue
            if i == 0 and j == 0:
                continue
            if matrix[r+i][c+j] == '#':
                num_occupied += 1
    return num_occupied


def num_occupied_2(matrix, r, c):
    num_occupied = 0
    moves = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    for move in moves:
        rnew = r
        cnew = c
        while True:
            rnew += move[0]
            cnew += move[1]
            if rnew < 0 or cnew < 0 or rnew >= len(matrix) or cnew >= len(matrix[0]):
                break
            if matrix[rnew][cnew] == '#':
                num_occupied += 1
                break
            if matrix[rnew][cnew] == 'L':
                break
    return num_occupied
            

def turn(matrix):
    new_matrix = [list(row) for row in matrix]
    made_change = False
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'L' and num_occupied_2(matrix, r, c) == 0:
                new_matrix[r][c] = '#'
                made_change = True
            elif matrix[r][c] == '.':
                new_matrix[r][c] = '.'
            elif matrix[r][c] == '#' and num_occupied_2(matrix, r, c) >= 5:
                new_matrix[r][c] = 'L'
                made_change = True
    return new_matrix, made_change


new_matrix = lines
while True:
    new_matrix, made_change = turn(new_matrix)
    if not made_change:
        c = 0
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[0])):
                if new_matrix[i][j] == '#':
                    c += 1
        print(c)
        break
