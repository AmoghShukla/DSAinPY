def SetMismatch(nums: list) -> list:
    n = len(nums)
    expected_sum = n * (n+1) // 2
    actual_sum = sum(nums)
    New_nums : list = []
    duplicate : int
    missing: int
    for i in nums:
        if i not in New_nums:
            New_nums.append(i)
        if i in New_nums:
            duplicate = i
    missing = expected_sum - (actual_sum - duplicate)

    return [duplicate, missing]