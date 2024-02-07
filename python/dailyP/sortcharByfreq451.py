import heapq
def frequencySort(s: str) -> str:
    charCount = {}
    for char in s:
        if char in charCount: charCount[char] += 1
        else: charCount[char] = 1
    
    max_heap = [(-freq, char) for char, freq in charCount.items()]
    heapq.heapify(max_heap)
    
    s = ""
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        s += char * (-freq)
    
    return s

s = "tree"
print(frequencySort(s))