def firstMissingPositiveId(ids: list[int]) -> int:

    setids = set(ids)
    smallnum = 1

    while smallnum in setids:
        smallnum +=1

    return smallnum



print(firstMissingPositiveId([1, 2, 4, 6]))        # expected: 3
print(firstMissingPositiveId([3, 4, 1, 2]))        # expected: 5
print(firstMissingPositiveId([2, 3, 7]))           # expected: 1
print(firstMissingPositiveId([1]))                 # expected: 2
print(firstMissingPositiveId([2]))                 # expected: 1
print(firstMissingPositiveId([1, 2, 3, 4, 5]))     # expected: 6
print(firstMissingPositiveId([1, 1, 2, 2, 3]))     # expected: 4
print(firstMissingPositiveId([5, 6, 7, 8]))        # expected: 1
print(firstMissingPositiveId([2, 1, 4, 3, 6]))     # expected: 5