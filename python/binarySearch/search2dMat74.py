# def searchMatrix(matrix: list[list[int]], target: int) -> bool:
#     row, col = len(matrix), len(matrix[0])
#     top, bot = 0, row - 1
#     while top <= bot:
#         mid_row = (top + bot) // 2
#         if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
#             l, r = 0, col
#             while l <= r:
#                 mid = (l + r) // 2
#                 if target == matrix[mid_row][mid]:
#                     return True
#                 elif target < matrix[mid_row][mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             return False
        
#         elif target < matrix[mid_row][0]:
#             bot = mid_row - 1
#         else:
#             top = mid_row + 1
    
#     return False

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row, col = len(matrix), len(matrix[0])
    l, r = 0, row*col - 1
    while l <= r:
        mid = (l+r) // 2
        if target == matrix[mid//col][mid%col]:
            return True
        elif target < matrix[mid//col][mid%col]:
            r = mid - 1
        else:
            l = mid + 1
    return False

mat = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
tar = 60
print(searchMatrix(mat, tar))