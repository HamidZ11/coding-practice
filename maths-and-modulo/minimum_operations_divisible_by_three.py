def minimumOperations(nums: list[int]) -> int:


    count = 0

    for num in nums:
        if num % 3 != 0:
            count += 1

    return count 




print(minimumOperations([1, 2, 3, 4]))   # expected: 3
print(minimumOperations([3, 6, 9]))      # expected: 0
print(minimumOperations([1]))            # expected: 1
print(minimumOperations([2]))            # expected: 1
print(minimumOperations([4, 5, 6]))      # expected: 2
print(minimumOperations([7, 8, 9]))      # expected: 2


