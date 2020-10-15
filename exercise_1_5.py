
def hotel_cost (nights):
    return 140*nights

def plain_ride_cost (city):
    if city == "Charlotte":
        return 183
    elif city =="Tampa" :
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = 40*days
    if days >6 :
        cost-=50
    elif days>=3 and days<7 :
        cost-=20
        return cost


def trip_cost(city,days):
    spending_money = rental_car_cost(days) + hotel_cost(days) + plain_ride_cost(city)
    return spending_money

print(trip_cost("Tampa",4))