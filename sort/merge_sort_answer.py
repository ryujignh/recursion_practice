import math

def merge(arr):
    return mergeHelper(arr, 0, len(arr) - 1)

def mergeHelper(arr, start, end):
    if start == end: return [arr[start]]
    middle = math.floor((start+end)/2)
    leftArr = mergeHelper(arr,start, middle)
    rightArr = mergeHelper(arr,middle+1,end)
    print(leftArr)
    print(rightArr)

    leftArr.append(math.inf)
    rightArr.append(math.inf)
    l = len(leftArr) + len(rightArr) - 2
    li = 0
    ri = 0
    merged = []

    while (li+ri) < l:
        if leftArr[li] <= rightArr[ri]:
            merged.append(leftArr[li])
            li = li+1
        else:
            merged.append(rightArr[ri])
            ri = ri+1

    return merged

# arr1 = [34,4546,32,3,2,8,6,76,56,45,34,566,1];
arr1 = [5,1,3];
print(arr1)
print(merge(arr1))