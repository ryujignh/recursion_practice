def largestRectangle(h):

    results = [0]*len(h)
    #nested for loops, O(n^2)
    for i in range(len(h)):
        j = i - 1
        total = 1
        curr = h[i]
        while j >= 0 and curr <= h[j]:
            total += 1
            j -= 1
        j = i + 1
        while j < len(h) and curr <= h[j]:
            total += 1
            j += 1
        results[i] = total * curr
    return max(results)

print(largestRectangle([3,2,3])) # 6
print(largestRectangle([1,2,5,2,3,4])) # 10
print(largestRectangle([1,2,3,4,5])) # 9
print(largestRectangle([3,4,5,8,10,2,1,3,9])) # 16
print(largestRectangle([1,2,1,3,5,2,3,4])) # 10
print(largestRectangle([11,11,10,10,10])) # 50
print(largestRectangle([8979,4570,6436,5083,7780,3269,5400,7579,2324,2116])) # 26152