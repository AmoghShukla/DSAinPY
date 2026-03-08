def findDissappearedNums(nums: list) -> list:
    Missing : list = []
    length : int  = len(nums)

    for i in nums:
        idx = abs(i) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    
    for i in range(length):
        if nums[i] > 0:
            Missing.append(i+1)
    return Missing