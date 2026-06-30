def expanded_form(num):
    place = 1
    ans = []
    while num > 0:
        mod = (num%10) * place
        if mod!=0:
            ans.append(str(mod))
        num = num // 10
        place *= 10
    ans.reverse()
    return " + ".join(ans)
        
        