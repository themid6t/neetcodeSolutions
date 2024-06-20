def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    pre, post = 1, 1
    for pr in range(n):
        res[pr] = pre
        pre *= nums[pr]

    for po in range(n-1, -1, -1):
        res[po] *= post
        post *= nums[po]
        print(post)

    return res

ar = [1,2,3,4]
print(productExceptSelf(ar))