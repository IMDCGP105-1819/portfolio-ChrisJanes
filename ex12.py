def hotel_cost(nights):
    return nights * 70

def plane_ticket_cost(city, flight_class):
    cost = 0
    if city == "New York":
        cost = 2000
    elif city == "Auckland":
        cost = 790
    elif city == "Venice":
        cost = 154
    else:
        cost = 65

    return round(cost * flight_class, 2)

def rental_car_cost(days):
    rental_cost = days * 30

    if days > 7:
        rental_cost -= 50
    elif days > 3:
        rental_cost -= 30

    return rental_cost

def total_cost(city, days, flight_class):
    cost = 0
    cost += hotel_cost(days-1)
    cost += plane_ticket_cost(city, flight_class)
    cost += rental_car_cost(days)

    return round(cost, 2)

print("plane cost:", plane_ticket_cost("New York", 1.0))
print("hotel:", hotel_cost(5))
print("car:", rental_car_cost(8))

print("total:", total_cost("Glasgow", 6, 1.9))