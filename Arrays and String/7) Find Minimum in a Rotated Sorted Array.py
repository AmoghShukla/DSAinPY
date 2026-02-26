def Find_Minimum(nums: list[int]) -> int:
    low = 0
    high = len(nums) - 1
    ans = nums[0]
    while(low <= high):
        mid = (low + high)//2
        if nums[high] > nums[low]:
            return min(ans, nums[low])
        if nums[mid] >= nums[low]:
            ans = min(ans, nums[low])
            low = mid + 1
        else:
            ans = min(ans, nums[mid])
            high = mid - 1
    return ans

nums = [4,5,6,7,0,1,2]
print(Find_Minimum(nums))