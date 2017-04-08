def find_missing(A, B):
    result = 0
    C = A + B
    for number in C:
        result ^= number  # XOR means 'strictly or', remember binary operators?

    return result   # or as a one liner; return reduce(lambda x, y: x^y, C)
    # if A == B:
    #     return 0
    # for num in C:
    #     if num in A and num in B:
    #         pass
    #     else:
            # result.append(num)
    #         return num
    # return result
    # for num in C:
    #     if C.count(num) % 2 != 0:
    #         # return num
    #         if num not in result:
    #             result.append(num)
    # return result


# print find_missing([9, 9, 7, 6, 5, 3, 4, 2, 1], [9, 7, 6, 5, 3, 4, 2, 1, 8])
# print find_missing([2], [2])
