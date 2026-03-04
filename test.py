def numSpecial(mat: list[list[int]]) -> int:
    row: int = len(mat)
    col: int = len(mat[0])
    Special = []
    for i in range(row - 1):
        for j in range(col - 1):
            row1 = mat[i]
            column = [row[j] for row in mat]
            if sum(row1) == 1 and sum(column) == 1:
                Special.append([i, j])
        
    return len(Special)

print(numSpecial([[1,0,0],[0,0,1],[1,0,0]]))