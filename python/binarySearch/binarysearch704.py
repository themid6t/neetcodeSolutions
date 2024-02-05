
def search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return 'Not Found'
        

ar = [-1,0,3,5,9,12]
tar = 9
print(search(ar, tar))