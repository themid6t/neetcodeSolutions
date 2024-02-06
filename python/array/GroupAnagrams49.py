
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     groups = {}
    
#     for string in strs:
#         count = [0] * 26
#         for char in string:
#             count[ord(char) - ord('a')] += 1
        
#         key = tuple(count)
#         if key not in groups:
#             groups[key] = []
#         groups[key].append(string)
    
#     return list(groups.values())

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    groups = {}
    for string in strs:
        product = 1
        for char in string:
            product *= primes[ord(char) - ord('a')]
        if product not in groups:
            groups[product] = []
        groups[product].append(string)
    
    return list(groups.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))