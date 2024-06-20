def characterReplacement(s: str, k: int) -> int:
    hashmap = {}
    res = 0
    
    maxf = 0
    l = 0
    for r in range(len(s)):
        hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
        maxf = max(maxf, hashmap[s[r]])
        while (r - l + 1) - maxf > k:
            hashmap[s[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
    return res

# def characterReplacement(s: str, k: int) -> int:
#     hashmap = {}
#     res = 0
#     l = 0
#     for r in range(len(s)):
#         hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
#         while (r - l + 1) - max(hashmap.values()) > k:
#             hashmap[s[l]] -= 1
#             l += 1
        
#         res = max(res, r - l + 1)
#     return res

# s, k = "AABABBA", 1
s, k = "ABAB", 2

print(characterReplacement(s, k))