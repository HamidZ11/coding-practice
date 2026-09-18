def minSubarrayLen(nums: list[int], target: int) -> int:

    left = 0
    min_length = float("inf")

    for right in range(len(nums)):

        sub_array = nums[left : right + 1]

        while sum(sub_array) >= target:
            current_length = right - left + 1
            min_length = min(min_length, current_length)
            left += 1
            sub_array = nums[left : right + 1]


    if min_length == float("inf"):
        return 0

    return min_length

print(minSubarrayLen([2, 3, 1, 2, 4, 3], 7))   # expected: 2
print(minSubarrayLen([1, 4, 4], 4))            # expected: 1
print(minSubarrayLen([1, 1, 1, 1], 5))         # expected: 0
print(minSubarrayLen([5], 5))                   # expected: 1
print(minSubarrayLen([2, 2, 2, 2], 6))         # expected: 3
print(minSubarrayLen([1, 2, 3, 4, 5], 11))     # expected: 3
print(minSubarrayLen([10, 1, 1], 9))            # expected: 1
print(minSubarrayLen([1, 2, 3], 100))           # expected: 0
print(minSubarrayLen([1, 1, 1, 7], 7))         # expected: 1
print(minSubarrayLen([3, 1, 1, 1, 3], 6))      # expected: 4