from collections import deque

lines = [int(l.strip()) for l in open('input.txt')]

def exists_sum(dq, r):
    s = set(dq)
    for n in s:
        if r - n in s:
            return True
    return False

# ----------- PART 1 -------------
dq = deque()
for i in range(25):
    dq.append(lines[i])

for num in lines[25:]:
    if not exists_sum(dq, num):
        print(num)
        break
    else:
        dq.popleft()
        dq.append(num)


# ----------- PART 2 -------------
INVALID = 373803594

# Definitely a faster O(..) way to do this
# but AOC input is not large enough to matter
for s_indx in range(0, len(lines)):
    for e_indx in range(s_indx+1, len(lines)+1):
        if sum(lines[s_indx:e_indx]) == INVALID:
            print(min(lines[s_indx:e_indx]) + max(lines[s_indx:e_indx]))
        elif sum(lines[s_indx:e_indx]) > INVALID:
            break