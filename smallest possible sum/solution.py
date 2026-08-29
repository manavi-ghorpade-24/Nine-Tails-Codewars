#calculate GCD for 2 elements because to stop comparison we need all elements to be equal 
def gcd(a,b):
    while b!=0:
        a, b =b, a%b
    return a

#we will calculate gcd for every element 
def solution(lst):
    g = lst[0]
    
    for num in lst[1:]:
        g = gcd(g,num)
        
    return g*len(lst) # smallest possible sum of all numbers in Array 