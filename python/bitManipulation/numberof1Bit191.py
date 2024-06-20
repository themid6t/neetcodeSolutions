"""
    Since we need to count the number of ones,
    Iteratively peform AND operation with 1 and add the result to count, if it is a one
    count increments else remains same, and shift n to the right by one bit.
"""

def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    
    return count