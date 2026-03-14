def getHappyString(n: int, k : int) -> str:
    res = []

    def backtrack(curr):
        if len(curr) == n:
            res.append(curr)
        
        for char in 'abc':
            if not curr or char != curr[-1]:
                backtrack(curr + char)
        
    backtrack('')
    return res[k-1] if k <= len(res) else ""