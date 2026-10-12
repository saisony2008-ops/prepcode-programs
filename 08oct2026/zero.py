
nums = list(map(int,input().split()))
for x in nums:
    if x ==0:
        nums.remove(0)
        nums.append(0)
print(nums)        
