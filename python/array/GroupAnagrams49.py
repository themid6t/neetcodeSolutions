
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    
    for string in strs:
        count = [0] * 26
        for char in string:
            count[ord(char) - ord('a')] += 1
        
        key = tuple(count)
        if key not in groups:
            groups[key] = []
        groups[key].append(string)
    
    return list(groups.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))