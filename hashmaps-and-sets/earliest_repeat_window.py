def earliestRepeatWithinWindow(nums: list[int], k: int) -> int:

    my_dict = {}

    for index, num in enumerate(nums):
        if num in my_dict:
            # if its already in the dictionary, check if that difference in the two indexes (index and my_dict[num][index] are k apart)
            if index - my_dict[num] <= k:
                return num
            else:
                my_dict[num] = index
        else:
            my_dict[num] = index

    return -1

print(earliestRepeatWithinWindow([1, 2, 3, 1, 4], 3))     # expected: 1
print(earliestRepeatWithinWindow([1, 2, 3, 1], 2))        # expected: -1
print(earliestRepeatWithinWindow([5, 6, 5, 7], 2))        # expected: 5
print(earliestRepeatWithinWindow([8, 8], 1))              # expected: 8
print(earliestRepeatWithinWindow([1, 2, 3, 4], 10))       # expected: -1
print(earliestRepeatWithinWindow([4, 1, 2, 4, 2], 2))     # expected: 2
print(earliestRepeatWithinWindow([9], 5))                  # expected: -1