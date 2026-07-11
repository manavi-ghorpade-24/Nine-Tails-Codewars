def sum_strings(x, y):
    i = len(x)-1
    j = len(y)-1
    
    carry = 0
    digit = 0
    mul = 1
    ans = []
    while i>=0 or j>=0 or carry:
        a = int(x[i]) if i>=0 else 0
        b = int(y[j]) if j>=0 else 0
        total =  a+b + carry
        ans.append(str(total%10))
        carry = total //10
        i -= 1
        j -= 1
    ans.reverse()
    result = "".join(ans).lstrip('0')
    return result if result else '0'
