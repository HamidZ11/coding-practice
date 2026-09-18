def longestIncreasingRun(nums: list[int]) -> int:

    max_run = 1
    prev_num = 0
    current_run = 1

    for i in range(1, len(nums)):

        if nums[i] > nums[prev_num]:
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 1

        prev_num += 1

    return max_run  




print(longestIncreasingRun([1, 2, 3, 4, 5]))        # expected: 5
print(longestIncreasingRun([5, 4, 3, 2, 1]))        # expected: 1
print(longestIncreasingRun([1, 2, 2, 3, 4]))        # expected: 3
print(longestIncreasingRun([5, 1, 2, 3, 0, 1]))     # expected: 3
print(longestIncreasingRun([-3, -2, -1, -5, -4]))   # expected: 3
print(longestIncreasingRun([1, 3, 2, 4, 3, 5]))     # expected: 2