def stockSpan(stocks):
    stack = []
    results = []

    for i in range(len(stocks)) :
        print(i)
        current = stocks[i]
        counter = 1

        while len(stack) > 0 and stocks[stack[-1]] < current: counter += results[stack.pop()]

        results.append(counter)
        stack.append(i)

    return results

print(stockSpan([30,50,60,20,30,64,80])) # [1,2,3,1,2,6,7]
print(stockSpan([24,5,67,60,24,64,23,536,345])) # [1,1,3,1,1,3,1,8,1]
print(stockSpan([200,85,40,60,40,65,90])) # [1,1,1,2,1,4,6]
print(stockSpan([30,45,20,100,235,300,4500,40,100])) # [1,2,1,4,5,6,7,1,2]
print(stockSpan([34,640,100,234,56,34,25,200,1020,160])) # [1,2,1,2,1,1,1,4,9,1]