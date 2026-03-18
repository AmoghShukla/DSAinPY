'''
Question : 3070
Title : Count Submatrices with Top-Left Element and Sum Less Than k
Difficulty : Medium

You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

Example 1:
Input: grid = [[1,1,1],[1,1,1],[1,1,1]], k = 4
Output: 4
Explanation: The submatrices that contain the top-left element of the grid and have a sum less than or equal to k are:
- The submatrix with the top-left element itself, which has a sum of 1.

'''

def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    counter = 0

    for i in range(m):
        for j in range(n):
            top = grid[i-1][j] if i>0 else 0
            left = grid[i][j=1] if j>0 else 0
            diagonal = grid[i-1][j-1] if i>0 and j > 0 else 0

            grid[i][j] += top + left - diagonal

            if grid[i][j] <= k:
                counter += 1

    return counter
