def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        curSum = numbers[left] + numbers[right]
        if curSum > target:
            right -= 1
        elif curSum < target:
            left += 1
        elif curSum == target:
            return [left+1, right+1]
    return None

ar = [2,7,11,15]
tar = 9
print(twoSum(ar, tar))