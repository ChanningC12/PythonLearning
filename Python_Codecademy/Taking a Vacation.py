def hotel_cost(nights):
    return 140*nights


def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475

print (plane_ride_cost("Tampa"))

def rental_car_cost(days):
    total=40*days
    if days>=7:
        total -= 50
    elif days>=3:
        total -= 20
    return total

print (rental_car_cost(7))

def trip_cost(city,days,nights):
    return rental_car_cost(days)+plane_ride_cost(city)+hotel_cost(nights)

print (trip_cost("Los Angeles",5,4))

#Add spending_money
def trip_cost(city,days,nights,spending_money):
    return rental_car_cost(days)+plane_ride_cost(city)+hotel_cost(nights)+spending_money

print (trip_cost("Los Angeles",5,4,1000))
