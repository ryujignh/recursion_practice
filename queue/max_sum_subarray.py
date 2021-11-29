def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    start = 0
    curr_sum = 0
    for end, val in enumerate(arr):
        curr_sum += val
        if end - start + 1 == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1

    return max_sum


arr = [2, 3, 4, 1, 5]
k = 3
print("expected:", 10)
print("actual", max_sum_subarray(arr, k))


