def solution(n, k):
    yangPrice = n*12000
    serviceDrink = int(n/10)
    paidDrink = k-serviceDrink
    drinkPrice = paidDrink*2000
    return yangPrice+drinkPrice