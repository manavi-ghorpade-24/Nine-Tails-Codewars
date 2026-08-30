def create_phone_number(n):
    #your code here
    ans = ''.join(map(str,n)) #map() applies str() to every element of n. 
    #join() takes an iterable of strings
    return f"({ans[:3]}) {ans[3:6]}-{ans[6:10]}"