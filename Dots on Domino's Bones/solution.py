def dots_on_domino_bones(n):
    sum = 0
    for i in range(n+1):
        for j in range(i,n+1):
            sum += i + j
    return sum