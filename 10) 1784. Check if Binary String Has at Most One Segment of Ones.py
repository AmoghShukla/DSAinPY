def checkOnesSegment(s: str) -> bool:
    seen_zero = False

    for char in s:
        if char == '1' and seen_zero  == True:
            return False
        elif char == '0':
            seen_zero = True
    return True

