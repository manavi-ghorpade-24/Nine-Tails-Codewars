def open_or_senior(data):
    ans = []
    for lst in data:
        if lst[0]>=55 and lst[1]>7:
            ans.append("Senior")
        else:
            ans.append("Open")
    return ans