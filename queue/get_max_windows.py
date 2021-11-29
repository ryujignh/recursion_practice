def getMaxWindows(arr, k):
    length = len(arr)
    results = []
    for i in range(length - k + 1):
        max_val = max(arr[i:k])
        results.append(max_val)
        k += 1
    return results

arr = [34,35,64,34,10,2,14,5,353,23,35,63,23]
k = 4
print("expected:", [64, 64, 64, 34, 14, 353, 353, 353, 353, 63])
print("actual", getMaxWindows(arr, k))

# getMaxWindows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4); #[64, 64, 64, 34, 14, 353, 353, 353, 353, 63]
