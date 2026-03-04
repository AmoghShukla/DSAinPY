'''
Question No. : 1545
Title : Find Kth Bit in Nth Binary String
Difficulty : Easy

Given a m x n binary matrix mat, return the number of special positions in mat. 
A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
'''

# Bruteforce approach

def numSpecial(mat: list[list[int]]) -> int:
    row = len(mat)
    col = len(mat[0])
    Special = []
    for i in range(row):
        for j in range(col):
            row1 = mat[i]
            column = [row[j] for row in mat]
            if sum(row1) == 1 and sum(column) == 1:
                Special.append([i, j])
    return len(Special)