def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    else:
        return 475
def rental_car_cost(days):
    if days >= 7:
        days = days*40
        total= days-50
    elif days>=3:
        days = days *40
        total = days -20
    else:
        total=days*40
    return total    
print hotel_cost(2)    
print plane_ride_cost("Pittsburgh")
print rental_car_cost(1)

def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print trip_cost("Los Angeles",5,600)
