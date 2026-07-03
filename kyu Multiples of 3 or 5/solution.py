def solution(number):
    if number <= 0:
        return 0
    def multiplications(k):
        count = (number-1) // k
        return k * count * (count+1) // 2
    return (multiplications(3) + multiplications(5) - multiplications(15))