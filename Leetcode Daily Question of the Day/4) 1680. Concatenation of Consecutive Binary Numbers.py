def concatenatedBinary(n: int) -> int:
    string = ""
    for i in range(1, n+1):
        binary = bin(i)[2:]
        string += binary
    integer = int(string, 2)
    if integer > 1000000007:
        return integer % 1000000007
    else:
        return integer

n = 12
print(concatenatedBinary(n))