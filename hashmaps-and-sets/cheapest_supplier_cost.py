def cheapestSupplierCost(
    numProducts: int,
    productId: list[int],
    price: list[int]
) -> int:


    for i in range(numProducts):
        if i not in productId:
            return -1
        else:
            