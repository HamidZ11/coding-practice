def longestStreak(nums: list[int]) -> int:

    left = 0
    right = len(nums) - 1
    zero_count = 0
    max_length = 0

    for right in range(len(nums)): # sliding window pattern
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1: # if you have more than one zero in your window
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        current_length = right - left + 1
        current_length -= 1 # because you remove exactly one element
        max_length = max(max_length, current_length)

    return max_length



print(longestStreak([1, 1, 0, 1]))          # expected: 3
print(longestStreak([1, 1, 1]))             # expected: 2
print(longestStreak([1, 0, 1, 1, 0, 1]))    # expected: 3
print(longestStreak([0, 0, 0]))             # expected: 0
print(longestStreak([1, 0, 1, 1, 1]))       # expected: 4
print(longestStreak([1]))                    # expected: 0
print(longestStreak([0, 1, 1, 1, 0]))       # expected: 3