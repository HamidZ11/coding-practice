def longestKDistinct(nums: list[int], k: int) -> int:
    left = 0
    counts = {}

    max_count = 0

    for right in range(len(nums)):
        num = nums[right]

        if num in counts: 
            counts[num] += 1
        else:
            counts[num] = 1

        while len(counts) > k:
            left_num = nums[left]
            counts[left_num] -= 1
            if counts[left_num] == 0:
                del counts[left_num]
            left += 1

        max_count = max(max_count, right - left + 1) # only want to measure outside of window once satisfied

    return max_count


    


print(longestKDistinct([1, 2, 1, 2, 3], 2))          # expected: 4
print(longestKDistinct([1, 2, 1, 3, 4, 2, 3], 3))    # expected: 4
print(longestKDistinct([5, 5, 5, 5], 1))              # expected: 4
print(longestKDistinct([1, 2, 3, 4], 1))              # expected: 1
print(longestKDistinct([1, 2, 3, 2, 2, 1], 2))        # expected: 4
print(longestKDistinct([1], 1))                        # expected: 1
print(longestKDistinct([1, 2, 1, 3, 4, 3, 5], 2))     # expected: 3
print(longestKDistinct([1, 1, 2, 2, 3, 3], 2))        # expected: 4