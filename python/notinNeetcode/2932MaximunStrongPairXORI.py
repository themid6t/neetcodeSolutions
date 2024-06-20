class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        """ Time Complexity: O(n^2)
            Space Complexity: O(1) """
        maxXOR = 0
        l, r = 0, 0

        while l < len(nums):
            if abs(nums[l] - nums[r]) <= min(nums[l], nums[r]):  # is Strong'
                isStrong = nums[l] ^ nums[r]
                if isStrong > maxXOR: 
                    maxXOR = isStrong
            
            r += 1
            if r == len(nums):
                l += 1
                r = l
            
        return maxXOR