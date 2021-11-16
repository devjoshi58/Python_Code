def BuySellStock(prices):

    buy_price = prices[0]
    profit = 0
    sell_price = 0

    for i in range(1,len(prices)):

        if prices[i]<buy_price:
            buy_price = prices[i]
        
        elif prices[i]>buy_price and profit< prices[i]-buy_price:
            sell_price = prices[i]
            profit = sell_price-buy_price

    print(profit)

BuySellStock([7,6,4,3,1,7])

BuySellStock([2,4,1])


#faster way
def maxProfit(self, prices: List[int]) -> int:
    
    if len(prices)<2:
        return 0
    
    
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    profit=0
    
    for i in range(1, len(prices)):

        profit = prices[i]-min_price
        
        max_profit = max(profit,max_profit)
        min_price = min(prices[i],min_price)

    if max_profit <0:
        return 0
    else:
        return max_profit