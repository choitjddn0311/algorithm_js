def solution(n, k):
    #양꼬치 총 먹은 갯수 * 가격
    yangPrice = n*12000
    # 서비스 받은 음료수 갯수
    serviceDrink = int(n/10)
    # 실제로 내야할 음료수 갯수
    paidDrink = k-serviceDrink
    # 실제로 내야할 음료수 가격
    drinkPrice = paidDrink*2000
    # 양꼬치 먹은갯수*가격 + 내야할 음료수 가격
    return yangPrice+drinkPrice