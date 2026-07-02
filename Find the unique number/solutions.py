def find_uniq(arr):
    # your code here
    comman = 0
    if arr[0] == arr[1]:
        comman = arr[0]
    elif arr[1] == arr[2]:
        comman = arr[1]
    else:
        comman = arr[0]
    
    for num in arr:
        if num !=comman:
            return num