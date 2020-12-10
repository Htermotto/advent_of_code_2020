nums = {int(l.strip()) for l in open('input.txt')}

# ------- PART 1 -----------
max_num = max(nums)
one_diff = 0
three_diff = 1
curr_volt = 0
while curr_volt <= max_num:
    if curr_volt + 1 in nums:
        one_diff += 1
        curr_volt += 1
    elif curr_volt + 2 in nums:
        curr_volt += 2
    elif curr_volt + 3 in nums:
        three_diff += 1
        curr_volt += 3
    else:
        print('CANNOT FIND SUITABLE VOLTS')
        break

print(one_diff * three_diff)

# --------- PART 2 -----------
# O(nlogn), DP == O(n), ways[i] = ways[i+1] + ways[i+2] + ways[i+3]

nums.add(max(nums) + 3)
nums.add(0)
nums = list(sorted(nums)) # O(nlogn)
ways = [0] * (len(nums))
ways[-1] = 1

for i in range(len(nums) - 2, -1, -1):
    for j in range(1, 4):
        if i + j >= len(nums):
            break

        if nums[i+j] - nums[i] > 3:
            break

        ways[i] += ways[i+j]

print(ways)