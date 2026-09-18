def cheapestDeliveryWindow(costs: list[int], k: int) -> int:

    min_cost = sum(costs[0:0 + k])
    min_index = 0

    for i in range(len(costs) - k + 1):
        new_array = costs[i:i + k]
        current_cost = sum(new_array)

        if current_cost < min_cost:
            min_cost = current_cost
            min_index = i

    return min_index
        
            




print(cheapestDeliveryWindow([4, 2, 1, 7, 3, 2], 3))  # expected: 0
print(cheapestDeliveryWindow([5, 1, 2, 1, 2], 2))     # expected: 1
print(cheapestDeliveryWindow([8, 3, 6], 3))           # expected: 0
print(cheapestDeliveryWindow([9, 1, 1, 9], 2))        # expected: 1
print(cheapestDeliveryWindow([3, 3, 3, 3], 2))        # expected: 0
print(cheapestDeliveryWindow([10, 5, 2, 1, 1], 1))    # expected: 3
print(cheapestDeliveryWindow([7], 1))                  # expected: 0
print(cheapestDeliveryWindow([6, 4, 5, 1, 2, 3], 3))  # expected: 3