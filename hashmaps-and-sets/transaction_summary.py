def transactionSummary(transactions):

    totals = {}
    best_category = None
    best_total = 0 

    # this now gives the amount for each transaction
    for transaction in transactions:
        category, amount = transaction.split()
        amount = int(amount)

        if category not in totals:
            totals[category] = amount
        else:
            totals[category] += amount

    for category, total in totals.items():
        if total > best_total:
            best_total = total
            best_category = category
        
    return best_category