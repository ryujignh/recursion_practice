arr = [34, 4546, 32, 3, 2, 8, 6, 76, 56, 45, 34, 566, 1]

def insertionSort(list):
    n = len(list)

    # 2
    for i in range(n):
        # list[2] = 32
        currentValue = list[i]

        # j = i - 1 = 2 - 1 = "1"
        for j in range(i - 1, -1, -1):
            # 32 <= 4536(list[1])
            if currentValue <= list[j]:
                list[j + 1] = list[j]
                list[j] = currentValue

    return list


print(arr)
insertionSort(arr)  # 昇順に並び替え
print(arr)  # ソートされた配列
