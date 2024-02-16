def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums)-1
    res = nums[0]
    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break

        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[left] <= nums[mid]:
            left = mid + 1
        else: right = mid - 1
    
    return res

# def findMin(nums: list[int]) -> int:
#     left, right = 0, len(nums) - 1
#     while left < right:
#         mid = left + (right - left) // 2
#         if nums[mid] < nums[right]:
#             right = mid
#         else:
#             left = mid + 1
#     return nums[left]

nums = [4,5,6,7,0,1,2]
print(findMin(nums))