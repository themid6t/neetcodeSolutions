def longestConsecutive(nums) -> int:
    nums = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in nums:
            length = 0
            while (n + length) in nums:
                length += 1
            longest = max(length, longest)
    return longest

ar = [100,4,200,1,3,2]
print(longestConsecutive(ar))