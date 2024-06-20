class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ Kadane's algorithm
            Time Complexity: O(n)
            Space Complexity: O(1) """
        largestSum = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0: curSum = 0
            curSum += num
            largestSum = max(largestSum, curSum)
        
        return largestSum