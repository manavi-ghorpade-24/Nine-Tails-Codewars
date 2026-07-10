def sum_of_intervals(intervals):
#     intervals.sort(...)   # modifies original list
#     sorted(intervals, ...) # returns a new sorted list
    intervals.sort(key = lambda x:x[0])
    first = intervals[0][0]
    last = intervals[0][1]
    ans = 0
    for int in intervals[1:]:
        if int[0] < last:
            last = max(last,int[1]) # imp to take max
                       
        else:
            ans += (last-first)
            first = int[0]
            last = int[1]
    ans += (last-first)
    return ans
        