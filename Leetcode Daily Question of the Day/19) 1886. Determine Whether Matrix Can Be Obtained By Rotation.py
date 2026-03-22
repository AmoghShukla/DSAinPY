def findRotation(mat, target) -> bool:
        for _ in range(4):
            if mat == target:
                  return True
            mat = [list(reversed(col)) for col in zip(*mat)]
        return False

mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
print(findRotation(mat, target))