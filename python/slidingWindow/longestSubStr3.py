# def lengthOfLongestSubstring(s: str) -> int:
#     left = 0
#     subs = ''
#     max_length = 0
#     for r in range(len(s)):
#         if s[r] not in subs:
#             subs += s[r]
#             max_length = max(max_length, r-left)
#         else:
#             left = s.find(s[r])+1
#             subs = subs[left:]
#     return max_length

def lengthOfLongestSubstring(s: str) -> int:
        char_idx = {}
        left, right = 0, 0
        max_length = 0 
        while right < len(s):
            if s[right] in char_idx and char_idx[s[right]] >= left:
                  left = char_idx[s[right]] + 1

            char_idx[s[right]] = right
            right += 1
            max_length = max(max_length, right - left)
        
        return char_idx, max_length

string = "abcabcbb"
print(lengthOfLongestSubstring(string))