def accum(st):
    ans = ""
    for c in range(0,len(st)):
        
        ans += (st[c] * (c+1)).capitalize() + "-"
    return ans[:-1]
        