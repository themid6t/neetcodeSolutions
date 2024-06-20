def trap(height: list[int]) -> int:
    maxl = [0] * len(height)
    maxr = [0] * len(height)
    l, r = 0, 0
    for i in range(len(height)-1, -1, -1):
        maxr[i] = r
        if height[i] > r:
            r = height[i]

    for i in range(0, len(height)):
        maxl[i] = l
        if height[i] > l:
            l = height[i]

    trapped = 0
    for i in range(len(height)):
        w = min(maxl[i], maxr[i]) - height[i]
        if w > 0:
            trapped += w    

    return trapped

    # return maxl, maxr, trapped

# def trap(height: list[int]) -> int:
#     l, r = 0, len(height)-1
#     maxl, maxr = height[0], height[-1]
#     trapped = 0
#     while maxl < maxr:
#         if maxl < maxr:
#             l += 1
#             maxl = max(maxl, height[l])
#         else:
#             r -= 1
#             maxr = max(maxr, height[r])
#         if min(maxl, maxr) - height[l] > 0:
#             trapped += (min(maxl, maxr) - height[l])
#     return trapped

h = [4,2,0,3,2,5]
print(trap(h))