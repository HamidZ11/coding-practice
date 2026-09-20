def maxSumDivThree(nums: list[int]) -> int:

    total = sum(nums)

    remainder_1 = [] # list of nums with remainder 1
    remainder_2 = [] # list of nums with remainder 2

    for num in nums:
        if num % 3 == 1:
            remainder_1.append(num)
        elif num % 3 == 2:
            remainder_2.append(num)

    remainder_1.sort()
    remainder_2.sort()

    if total % 3 == 0:
        return total
    
    elif total % 3 == 1: 
        # if the remainder is 1, then you either need 1 number with a remainder of 1 
        # to leave the list, or 2 with a remainder of 2 each, 
        # remove whichever one is smaller
        candidates = []

        if len(remainder_1) >= 1: # this is error handling for the case that there are no numbers in the list with remainder 1
            first_total = total - min(remainder_1) 
            candidates.append(first_total)

        if len(remainder_2) >= 2:
            second_total = total - (remainder_2[0] + remainder_2[1])
            candidates.append(second_total)

        total = max(candidates)

    else:
        candidates = []

        if len(remainder_1) >= 2:
            first_total = total - (remainder_1[0] + remainder_1[1])
            candidates.append(first_total)

        if len(remainder_2) >= 1:
            second_total = total - remainder_2[0]
            candidates.append(second_total)

        total = max(candidates)

    return total





print(maxSumDivThree([3, 6, 5, 1, 8]))   # expected: 18
print(maxSumDivThree([4]))                # expected: 0
print(maxSumDivThree([1, 2, 3, 4, 4]))   # expected: 12
print(maxSumDivThree([3, 3, 3]))          # expected: 9
print(maxSumDivThree([1, 1, 1]))          # expected: 3
print(maxSumDivThree([2, 2, 2, 2]))       # expected: 6
print(maxSumDivThree([5, 2, 2, 2]))       # expected: 9