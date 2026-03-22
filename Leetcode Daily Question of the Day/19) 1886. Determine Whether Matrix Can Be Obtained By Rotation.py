def findRotation(mat, target) -> bool:
        for _ in range(4):
            if mat == target:
                  return True
            mat = [list(reversed(col)) for col in zip(*mat)]
        return False