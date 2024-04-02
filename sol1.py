def find_profit(prices):
    buy, sell = 0,1
    max_profit  =0
    profit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)

        else:
            buy +=1
        sell +=1
    print(max_profit)

find_profit([12,24,35])