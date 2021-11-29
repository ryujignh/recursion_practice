arr = [34, 4546, 32, 3, 2, 8, 6, 76, 56, 45, 34, 566, 1]

def selectionSort(list):
    n = len(list)

    for i in range(0, n):
        minIndex = i

        for j in range(i + 1, n):
            if list[j] < list[minIndex]:
                minIndex = j

        temp = list[i]
        list[i] = list[minIndex]
        list[minIndex] = temp

    return list





































# def selectionSort(list):
#     n = len(list)
#
#     for i in range(0, n):
#         minIndex = i  # i番目の値を暫定の最小値をする
#         for j in range(i + 1, n):
#             if list[j] <= list[minIndex]:  # もし暫定の最小値以下なら最小値を更新
#                 minIndex = j
#
#         # list[i]とlist[minIndex]の入れ替え
#         temp = list[i]
#         list[i] = list[minIndex]
#         list[minIndex] = temp
#
#     return list


# def selectionSort(list):
#     n = len(list)
#     for i in range(n):
#         minIndex = i  # i番目の値を暫定の最小値とします。
#         for j in range(i + 1, n):
#             if list[j] <= list[minIndex]:  # 暫定の最小値以下なら最小値を更新
#                 minIndex = j  # 最小値を持つ
#
#         # list[i]とA[minIndex]の入れ替え
#         temp = list[i]
#         list[i] = list[minIndex]
#         list[minIndex] = temp


print(arr)
selectionSort(arr)  # 昇順に並び替え
print(arr)  # ソートされた配列
