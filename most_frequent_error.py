def mostFrequentError(errors: list[int]) -> int:

    newdict = {}

    for i in errors:
        if i in newdict:
            newdict[i] += 1
        else:
            newdict[i] = 1

    best_error = None
    best_count = 0

    for error, count in newdict.items():
        if count > best_count:
            best_count = count
            best_error = error

    return best_error

# The code accounts for tie scenarios 
# because dictionaries preserve insertion order


print(mostFrequentError([500, 404, 500, 403, 404, 500]))  # expected: 500
print(mostFrequentError([404, 500, 500, 404]))            # expected: 404
print(mostFrequentError([403]))                           # expected: 403
print(mostFrequentError([200, 201, 202, 200, 201, 202])) # expected: 200
print(mostFrequentError([500, 500, 404, 404, 403]))       # expected: 500
print(mostFrequentError([100, 200, 300, 400]))            # expected: 100
print(mostFrequentError([599, 599, 599, 100]))            # expected: 599