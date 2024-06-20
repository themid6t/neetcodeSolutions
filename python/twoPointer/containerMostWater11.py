# def maxArea(height: list[int]) -> int:
#     # Brute force
#     m = []
#     for i in range(len(height)):
#         for j in range(i+1, len(height)):
#             h = min(height[i], height[j])
#             w = (j - i)
#             m.append(w*h)
#     return sorted(m)[-1]

def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        if area > max_area: max_area = area
        if height[l] > height[r]: 
            r -= 1
            continue
        l += 1
    
    return max_area

arr = [1,8,6,2,5,4,8,3,7]
# arr = [1, 1]
print(maxArea(arr))