def solve(nums):
    s = sorted(nums) # [2, 4, 5, 8, 11]
    count = 0
    for i in range(len(nums)):
        if s[i] == nums[i]:
            count += 1
    return count
print(solve([2, 8, 4, 5, 11]))