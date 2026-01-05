def solution(s1, s2):
    # count = 0
    # for i in s1:
    #     if i in s2:
    #         count += 1
    # return count
    
    # set() 은 집합 자료형을 만들수 있게하는 함수
    # ex) 교집합, 차집합, 합집합 등등
    return len(set(s1)&set(s2))