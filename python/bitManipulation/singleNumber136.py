"""
    XOR operation --> 1 ^ 1 = 0
                      0 ^ 0 = 0 
                      1 ^ 0 = 1
                      0 ^ 1 = 1
    We can use Xor operation among all the numbers in the array, and we will
    be left with the single number, since any two same numbers will have the
    same binary representations, and xor operation between them will lead to zero
    and we will be left with the single number since 0 ^ 1 is 1. 
"""


def singleNumber(nums: list[int]) -> int:
    res = 0
    for i in range(len(nums)):
        res ^= nums[i]
    
    return res

