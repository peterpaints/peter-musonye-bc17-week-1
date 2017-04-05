def find_missing(A, B):
    result = 0
    C = A + B
    for number in C:
        result ^= number  # XOR means 'strictly or', remember binary operators?

    return result   # or as a one liner; return reduce(lambda x, y: x^y, C)


# print find_missing([2], [2])
