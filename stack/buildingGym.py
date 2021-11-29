from collections import deque

def stackCounter(arr):
    # Contains indexes
    stack = []
    results = [0] * len(arr)
    i = 0
    for x in arr:
        total = 1
        while len(stack) != 0 and arr[stack[-1]] >= x:
            j = stack.pop()
            total += results[j]

        stack.append(i)
        results[i] = total
        i += 1

    return results


def largestRectangle(h):
    left = stackCounter(h)

    # Right needs to be reversed in order to reuse the stackCounter,
    # then, re-reverse the result in order to get the correct results
    right = stackCounter(h[::-1])[::-1]

    total = [ (left[i] + right[i] - 1) * h[i] for i in range(len(h)) ]
    return max(total)

# print(largestRectangle([2, 1, 5, 6, 2, 3]))  # --> 6
print(largestRectangle([1, 2, 1, 3, 5, 2, 3, 4]))  # --> 6
# print(largestRectangle([3, 2, 3]))  # --> 6
# print(largestRectangle([1, 2, 5, 2, 3, 4]))  # --> 10
# print(largestRectangle([1, 2, 3, 4, 5]))  # --> 9
