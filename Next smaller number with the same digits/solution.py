def next_smaller(n):
    digits = list(str(n))
    for i in range(len(digits)-2, -1, -1):
        a =int(digits[i])
        b =int(digits[i+1])
        if a > b:
            pivot = a
            max = float('-inf')
            maxj = -1
            for j in range(i+1, len(digits)):
                if int(digits[j]) < pivot and max < int(digits[j]):
                    max = int(digits[j])
                    maxj = j
        
            digits[i] = str(max)
            digits[maxj] = str(a)
            digits[i+1:] = sorted(digits[i+1:],reverse=True)
            
            if digits[0] == '0':
                return -1
            return int("".join(digits))
    return -1
    
            
                
            