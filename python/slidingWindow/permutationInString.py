def checkInclusion(s1: str, s2: str) -> bool:
    s1_map = {}
    for c in s1:
        s1_map[c] = 1 + s1_map.get(c, 0)

    s2_map = {}
    window = len(s1)

    for i, c in enumerate(s2):
        s2_map[c] = 1 + s2_map.get(c, 0)
        if i >= window:
            if s2_map[s2[i - window]] == 1:
                del s2_map[s2[i - window]]
            else:
                s2_map[s2[i - window]] -= 1
        if i >= window - 1 and s1_map == s2_map:
            return True
    
    return False
    
# s1, s2 = "ab", "eidbaooo"

s1, s2 ="hello", "ooolleoooleh"

print(checkInclusion(s1, s2))