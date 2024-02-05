# def threeSum(nums: list[int]) -> list[list[int]]:
#     res = []
#     nums.sort()
#     if len(nums) <= 3: return []
#     for i, a in enumerate(nums):
#         if i > 0 and a == nums[i - 1]:
#             continue

#         l, r = 1, len(nums)-1
#         while l < r:
#             print(a, l, r)
#             s = nums[a] + nums[l] + nums[r]
#             if s == 0:
#                 res.append([nums[a], nums[l], nums[r]])
#                 l += 1; r -= 1
#             elif s > 0:
#                 r -= 1
#             else:
#                 l += 1
#     return res

    
def threeSum(nums):
    res = []
    nums.sort()
    if len(nums) < 3: return None
    print(nums)
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]: continue
        
        l, r = i, len(nums)-1
        while l < r:
            s = a + nums[l] + nums[r]
            if s == 0:
                res.append([a, nums[l], nums[r]])
                l += 1; r -= 1
                while nums[l] == nums[l-1] and l < r: l += 1
            elif s > 0:
                r -= 1
            else:
                l += 1
    return res

# ar = [-1,0,1,2,-1,-4]
ar = [0, 0, 0, 0, 0]
print(threeSum(ar))