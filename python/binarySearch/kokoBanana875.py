from math import ceil
def minEatingSpeed(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)+1
    k = 0
    while left < right:
        mid = left + ((right - left) // 2)
        time_taken = sum(ceil(p / mid) for p in piles)
        # print(f"{left} {mid} {right}, {time_taken}", end='\r')
        if time_taken <= h:
            k = mid
            right = mid
        else:
            left = mid+1
    return k



# def minEatingSpeed(piles: list[int], h: int) -> int:
#     ## brute force solution
#     speed_set = range(1, max(piles)+1)
#     for k in speed_set:
#         time_taken = 0
#         for pile in piles:
#             time_taken += ceil(pile / k)
#         print(f"{k}, {time_taken}", end="\r")
#         if time_taken <= h:
#             return k


# piles = [3,6,7,11]
piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))