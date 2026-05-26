def maximumAmount(coins: List[List[int]]) -> int:
        i, j = 0, 0
        current_amt = 0
        while i < len(coins) and j < len(coins[0]):
            if coins[i+1][j] >= coins[i][j+1]:
                if coins[i+1][j] < 0:
                    current_amt -= coins[i+1][j]
                else:
                    current_amt -= coins[i+1][j]
                i += 1
            else:
                current_amt += coins[i][j+1]
                j += 1
        return current_amt


coins  = [[0,1,-1],[1,-2,3],[2,-3,4]]
print(maximumAmount(coins))