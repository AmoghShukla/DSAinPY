'''
Question : 1886
Title : Determine Whether Matrix Can Be Obtained By Rotation
Difficulty : Easy

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
'''


def findRotation(mat, target) -> bool:
        
        for i in range(4):
            if mat == target:
                  return True
            mat = [list(reversed(col)) for col in zip(*mat)]
        return False

mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]
print(findRotation(mat, target))