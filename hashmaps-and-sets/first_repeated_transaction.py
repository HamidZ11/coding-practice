def firstRepeatedTransaction(transactions: list[int]) -> int:

    min_index = 0

    tset = set()

    for num in transactions: 
        if num in tset:
            return num
        else: 
            tset.add(num)

    return -1

        



print(firstRepeatedTransaction([10, 4, 7, 10, 4]))  # expected: 10
print(firstRepeatedTransaction([5, 1, 2, 3, 2, 1]))  # expected: 2
print(firstRepeatedTransaction([1, 2, 3, 4]))         # expected: -1
print(firstRepeatedTransaction([9, 9]))               # expected: 9
print(firstRepeatedTransaction([1, 2, 1, 2]))         # expected: 1
print(firstRepeatedTransaction([3, 3, 3]))            # expected: 3
print(firstRepeatedTransaction([7]))                  # expected: -1