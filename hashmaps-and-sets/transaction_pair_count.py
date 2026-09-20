class Solution:
    def countPairs(self, transactions: list[int], target: int) -> int:
        pair_count = 0
        hash_map = {} # stores the numbers we have seen and how mnay times weve seen them

        for i in transactions:
            # Find the value needed to pair with i
            # so that the two numbers add up to target
            need = target - i

            # If we have seen the needed value before,
            # each occurrence creates a new valid pair
            if need in hash_map:
                pair_count += hash_map[need]

            # Record the current number AFTER checking for a pair.
            # This prevents the current element from pairing with itself.
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        return pair_count