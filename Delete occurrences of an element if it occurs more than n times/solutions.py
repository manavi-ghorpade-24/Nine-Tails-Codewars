from collections import defaultdict
def delete_nth(order,max_e):
    mp = defaultdict(int)
    ans = []
    for num in order:
        if mp[num]>=max_e:
            pass
        else:
            mp[num] += 1
            ans.append(num)
    return ans
            
        
    