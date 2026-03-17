'''
Question: 1727
Title: Largest Submatrix With Rearrangements
Difficulty: Medium
Given a binary matrix, we can rearrange the columns of the matrix in any order. After rearranging the columns, return the area of the largest submatrix that only contains 1's.
Return the area of the largest submatrix within the rearranged matrix that only contains 1's.
Example 1:
Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4

'''

class Solution:
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                max_area = max(max_area, row[j] * (j + 1))
        
        return max_area
    

matrix = [[0,0,1],[1,1,1],[1,0,1]]
print(Solution().largestSubmatrix(matrix))