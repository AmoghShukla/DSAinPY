'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''

def StockSalesPredictor(prices : list[int]) -> int:
    if not prices:
        return 0
    
    pointer_1 : int= 0
    pointer_2 : int= pointer_1 + 1
    output_list : list[int] = []

    while(pointer_2 < len(prices)):
        diff = pointer_2 - pointer_1
        if prices[pointer_2] > prices[pointer_1]:
            pointer_2 += 1
        elif prices[pointer_2] < prices[pointer_1] and diff >= 1:
            output_list.append([[pointer_1], [pointer_2]])
            pointer_1 = pointer_2
            pointer_2 = pointer_1 + 1
        pointer_1 += 1
        pointer_2 += 1
    return output_list
prices = [7,1,2,3,5,3,4,6,4,7,9,11,12,15,22,23,21]
print(StockSalesPredictor(prices))