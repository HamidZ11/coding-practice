def firstDuplicateWithinK(nums: list[int], k: int) -> int:

    my_dict = {}

    for index, num in enumerate(nums):

        if num in my_dict:
            our_gap = index - my_dict[num]
            if our_gap <= k:
                return num
            else:
                my_dict[num] = index
        else:
            my_dict[num] = index 

    return -1

print(firstDuplicateWithinK([4, 2, 7, 4, 8, 2], 3))  # expected: 4
print(firstDuplicateWithinK([1, 2, 3, 1], 2))        # expected: -1
print(firstDuplicateWithinK([5, 1, 2, 1, 5], 2))     # expected: 1
print(firstDuplicateWithinK([7, 7], 1))              # expected: 7
print(firstDuplicateWithinK([1, 2, 3, 4], 10))       # expected: -1
print(firstDuplicateWithinK([3, 1, 3, 1], 1))        # expected: -1