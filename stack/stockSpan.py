# def stockSpan(stocks):
#     results = []
#
#     for idx, val in enumerate(stocks):
#         stockSpan = getStockSpan(stocks, idx)
#         results.append(stockSpan)
#
#     return results
#
#
# def getStockSpan(stocks, idx):
#     pointer = idx - 1
#
#     while pointer >= 0 and stocks[pointer] < stocks[idx]:
#         pointer -= 1
#
#     return idx - pointer
#
# print(stockSpan([30,50,60,20,30,64,80])) #[1,2,3,1,2,6,7]

def stockSpan(stocks):
    results = []

    # Save idx
    stack = []

    for i in range(len(stocks)):
        counter = 1
        current = stocks[i]

        # stocks[stack[len(stack)-1]]でpeakをゲットする
        while len(stack) > 0 and stocks[stack[len(stack) - 1]] < current:
            print(len(stack))
            pop = stack.pop()
            counter += results[pop]

        # print(counter)

        results.append(counter)
        stack.append(i)

    return results

print(stockSpan([30,50,60,20,30,64,80])) #[1,2,3,1,2,6,7]