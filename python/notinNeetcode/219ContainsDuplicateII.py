# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         index_map = {}
                
#         for i, num in enumerate(nums):
#             if num in index_map and i - index_map[num] <= k:
#                 return True
#             index_map[num] = i
        
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """ Time Complexity: O(n)
            Space Complexity: O(min(n, k)) 
            as window will contain atmost k+1 elements at the worst case"""
        
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])

        
        return False