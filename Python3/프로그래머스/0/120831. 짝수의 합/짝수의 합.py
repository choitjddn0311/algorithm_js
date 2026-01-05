def solution(n):
    result = 0
    # range의 기능을 활용해 0부터 n+1까지 진행되는데 2씩 더해나가면서 진행됨
    for i in range(0, n+1, 2):
        result += i
        
    return result