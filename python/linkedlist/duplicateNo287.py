class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = set()
        for i in range(len(nums)):
            if nums[i] in n: return nums[i]
            n.add(nums[i])

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         fast, slow = 0, 0
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break
#         slow2 = 0
#         while True:
#             slow = nums[slow]
#             slow2 = nums[slow2]
#             if slow == slow2:
#                 return slow