def firstPeakValue(nums: list[int]) -> int:


    for i in range(1, len(nums) - 1):

        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return nums[i]

    return -1



print(firstPeakValue([1, 4, 2, 5, 3]))       # expected: 4
print(firstPeakValue([1, 2, 3, 4]))          # expected: -1
print(firstPeakValue([5, 3, 1]))             # expected: -1
print(firstPeakValue([1, 3, 1]))             # expected: 3
print(firstPeakValue([2, 5, 5, 2]))          # expected: -1
print(firstPeakValue([9]))                    # expected: -1
print(firstPeakValue([1, 2]))                 # expected: -1
print(firstPeakValue([3, 1, 7, 2, 8, 1]))    # expected: 7