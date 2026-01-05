def solution(num_list):
    j = 0
    h = 0
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            j += 1
        else:
            h += 1
    return [j,h]