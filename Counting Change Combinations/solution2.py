def count_change(money, coins):
    # your implementation here
    if not coins:
        return 1
    res = []
    cur = []
    def back(idx, tar):
        if tar == 0:
            res.append(cur.copy())
            return
        for j in range(idx, len(coins)):
            if coins[j]<=tar:
                cur.append(coins[j])
                back(j, tar-coins[j])
                cur.pop()
    
    back(0,money)
    return len(res)