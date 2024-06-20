import heapq
def topKFrequent(nums: list[int], k: int) -> list[int]:
    table = {}
    for num in nums:
        if num not in table:
            table[num] = 1
        table[num] += 1
    table = [(-value, key) for key, value in table.items()]
    heapq.heapify(table)

    return [heapq.heappop(table)[1] for i in range(k)]

ar = [1,1,1,2,2,3]
print(topKFrequent(ar, 2))