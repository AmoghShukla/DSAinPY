
# # Bruteforce
# def search(self, nums: List[int], target: int) -> int:
#     if target in nums:
#         return nums.index(target)
#     else:
#         return -1

def search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = (low + high)//2

        # changed this : 

        # if nums[high] == target:
        #     return high
        # if nums[low] == target:
        #     return low
        # if nums[mid] == target:
        #     return mid

        # to this
        
        for i in [mid, low, high]:
            if nums[i] == target:
                return i
        if nums[mid] >= target:
            low = mid + 1
        else:
            high = mid - 1
    return low
            


nums = [4,5,6,7,0,1,2] 
target = 0

print(search(nums, target))