def alphabet_war(fight):
    left = {"w":4,"p":3,"b":2,"s":1}
    right = {"m":4, "q":3, "d":2,"z":1}
    right_score = 0
    left_score = 0
    for i in range(len(fight)):
        if i-1>0 and fight[i-1] == "*":
            pass
        
        elif i+1<len(fight) and fight[i+1]=="*":
            pass
        
        else:
            if fight[i] in left:
                left_score = left_score + left[fight[i]]
            if fight[i] in right:
                right_score = right_score + right[fight[i]]
    if left_score>right_score:
        return "Left side wins!"
    elif left_score<right_score:
        return "Right side wins!"
    return "Let's fight again!"