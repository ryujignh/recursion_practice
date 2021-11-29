import math
import pdb
from IPython import embed

arr = [34, 4546, 32, 3, 2, 8, 6, 76, 56, 45, 34, 566, 1]
# arr = [34, 4546, 32, 3, 2, 8, 6, 76]


def merge(arr):
    # return mergeSort(arr, 0, len(arr) - 1)
    return mergeSort(arr)


def mergeSort(arr):
    n = len(arr)
    if len(arr) == 1:
        return arr

    middle = math.floor(n / 2)
    print(middle)
    print(arr)
    sortedLeft = mergeSort(arr[0:middle-1])
    print(sortedLeft)
    sortedRight = mergeSort(arr[middle:n])
    merged = []
    li = 0
    l = len(sortedLeft)
    while li < l:
        merged.append(sortedLeft[0])
        li += 1
    # while len(sortedLeft) > 0 and len(sortedRight) > 0:
    #     if sortedLeft[0] > sortedRight[0]:
    #         merged.append(sortedRight.pop(0))
    #         merged.append(sortedLeft.pop(0))
    #     else:
    #         merged.append(sortedLeft.pop(0))
    #         merged.append(sortedRight.pop(0))
    return merged

print(arr)
arr = merge(arr)  # 昇順に並び替え
print(arr)  # ソートされた配列
