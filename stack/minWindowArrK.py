def minWindowArrK(intArr, k):
    results = []

    i = 0
    while i + k <= len(intArr):
        start = i
        end = i + k
        subArr = intArr[start:end]
        minVal = min(subArr)
        results.append(minVal)
        i += 1

    return results


print(minWindowArrK([2, 3, 1, 1, 12, 3, 10], 1))  # [2,3,1,1,12,3,10]
