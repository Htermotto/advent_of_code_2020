nums = [1,12,0,20,8,16]

last_seen = {n: [(i+1)] for i, n in enumerate(nums)}
del last_seen[16]

i = len(nums)
last_spoken = nums[-1]
for i in range(len(nums), 30000000):
    if last_spoken in last_seen:
        n = i - last_seen[last_spoken][-1]
        last_seen[last_spoken].append(i)
        last_spoken = n
    else:
        last_seen[last_spoken] = [i]
        last_spoken = 0

print(last_spoken)
