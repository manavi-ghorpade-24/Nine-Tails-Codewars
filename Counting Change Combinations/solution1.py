def count_change(money, coins):
    # your implementation here
    if not coins:
        return 1
    res = []
    cur = []
    def back(i, tar):
        if i >= len(coins):
            return
        if tar == 0:
            res.append(cur.copy())
            return
        if tar>=coins[i]: #pick same
            cur.append(coins[i])
            back(i, tar-coins[i])
            cur.pop()
        back(i+1, tar) #pick diff
    
    back(0,money)
    return len(res)