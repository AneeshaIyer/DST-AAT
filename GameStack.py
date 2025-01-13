def GameStack(maxSum, a, b):
    sums = 0
    count = 0
    score = 0
    i = 0
    while i < len(a) and sums + a[i] <= maxSum:
        sums += a[i]
        count += 1
        i += 1
    score = count  #
    j = 0
    while i > 0:
        i -= 1
        sums -= a[i]
        count -= 1
        while j < len(b): 
            if sums + b[j] <= maxSum:
                sums += b[j]
                count += 1
                score = max(score, count)
                j += 1
            else:
                break 
    return score

n = int(input()) 
for i in range(n):
    n1, m, maxSum = map(int, input().split()) 
    a = list(map(int, input().split())) 
    b = list(map(int, input().split()))
    print(GameStack(maxSum, a, b))
