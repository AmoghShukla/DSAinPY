'''
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
A grid is said to be valid if all the cells above the main diagonal are zeros.
Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

level : Medium

Example : 
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
'''

class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        zeros = []

        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        swaps = 0

        for i in range(n):
            needed = n - i - 1
            j = i
            while j < n and zeros[j] < needed:
                j += 1
            if j == n:
                return -1
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                j -= 1
                swaps += 1

        return swaps


grid = [[0,0,1],[1,1,0],[1,0,0]]
print(minSwaps(grid))