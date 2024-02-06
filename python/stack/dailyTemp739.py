# def dailyTemperatures(temperatures: list[int]) -> list[int]:
#     """ Brute force """
#     result = [0] * len(temperatures)
#     for temp in range(len(temperatures)):
#         for n in range(temp+1, len(temperatures)):
#             if temperatures[temp] < temperatures[n]:
#                 result[temp] = n - temp
#                 break
    
#     return result

from collections import deque

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    length = len(temperatures)
    result = [0] * length
    stack = deque()
    for idx, temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            _, prev_idx = stack.pop()
            result[prev_idx] = idx - prev_idx
        stack.append((temp, idx))
    return result


temp = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temp))