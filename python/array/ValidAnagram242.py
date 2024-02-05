
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):    # if the length of the strings are not equal
        return False        # they cannot be anagram
    
    charCount = [0] * 26    # to keep count of the characters in the string 

    for i in range(len(s)):
        # ord return unicode and maps in range 0-26
        charCount[ord(s[i]) - ord('a')] += 1    # increment in count
        charCount[ord(t[i]) - ord('a')] -= 1    # decrement in count for the same alphabet
    # if in the end all the counts in the array are not equal then it is not a valid anagram
    return all(count == 0 for count in charCount)
