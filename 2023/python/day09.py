from numpy import cumsum

with open("input.txt") as f:
    lines = f.read().strip().splitlines()  

def sol(p):
    total = 0
    for l in lines:
        nums, lasts = list(map(int, l.split() if p == 1 else reversed(l.split()))), []
        while any(nums):
            lasts.append(nums[-1]) 
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        total += cumsum(lasts)[-1]
    return total
    
print(sol(1), sol(2))       