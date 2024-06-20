def maxProfit(prices: list[int]) -> int:
    maxP = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            pf = prices[r] - prices[l]
            maxP = max(maxP, pf)
        else:
            l = r
        r += 1
    
    return maxP
        

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
