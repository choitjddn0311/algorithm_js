def solution(n):
    s = list(str(n))
    result = 0
    for i in range(len(s)):
        result += int(s[i])
        
    return result