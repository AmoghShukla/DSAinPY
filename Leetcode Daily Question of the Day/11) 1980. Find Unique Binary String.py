def findDifferentBinaryString(nums: list[str]) -> str:
    length = len(nums[0])
    val = 2 ** length

    
    for i in range(val):
        binary_value = bin(i)[2:].zfill(length)
        if str(binary_value) not in nums:
            return str(binary_value)
