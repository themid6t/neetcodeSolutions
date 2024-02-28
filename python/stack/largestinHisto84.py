def largestRectangleArea(heights: list[int]) -> int:
    maxArea = 0
    stack = [] # (index, height)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, (i - index) * height)
            start = index
        stack.append((start, h))
    
    for i, h in stack:
        maxArea = max(maxArea, (len(heights) - i) * h)

    return maxArea

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))