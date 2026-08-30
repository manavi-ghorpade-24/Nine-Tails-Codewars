def create_phone_number(n):
    #your code here
    #just converting int to string 
    ans = ""
    if len(n)<10:
        return ans
    ans += "(" 
    for i in range(0,3):
        ans += str(n[i])
    ans += ") "
    for i in range(3,6):
        ans += str(n[i])
    ans += "-"
    for i in range(6,10):
        ans += str(n[i])
    
#     print(ans)
    return ans
    