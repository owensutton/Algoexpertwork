def twoNumberSum(array, targetSum):
    out = []
    for x in array:
        for y in array:
            if x + y == targetSum:
                out.append(x)
                out.append(y)
    print out




twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10)