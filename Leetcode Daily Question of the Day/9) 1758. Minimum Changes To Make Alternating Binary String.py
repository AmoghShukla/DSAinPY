def minOperations(s: str) -> int:
    counter1 : int = 0
    counter2 : int = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                counter1 += 1
            if s[i] != '1':
                counter2 += 1
        else:
            if s[i] != '1':
                counter1 += 1
            if s[i] != '0':
                counter2 += 1
        
    return min(counter1, counter2)

s = '10010100'
print(minOperations(s))

        