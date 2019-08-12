from ex12 import *

def test_hotel_cost():
    assert hotel_cost(5) == 350

def test_plane_ticket_cost_economy():
    assert plane_ticket_cost("New York", 1.0) == 2000
    assert plane_ticket_cost("Auckland", 1.0) == 790
    assert plane_ticket_cost("Venice", 1.0) == 154
    assert plane_ticket_cost("Glasgow", 1.0) == 65

def test_plane_ticket_cost_premium():
    assert plane_ticket_cost("New York", 1.3) == 2600
    assert plane_ticket_cost("Auckland", 1.3) == 1027
    assert plane_ticket_cost("Venice", 1.3) == 200.20
    assert plane_ticket_cost("Glasgow", 1.3) == 84.50

def test_plane_ticket_cost_business():
    assert plane_ticket_cost("New York", 1.6) == 3200
    assert plane_ticket_cost("Auckland", 1.6) == 1264
    assert plane_ticket_cost("Venice", 1.6) == 246.40
    assert plane_ticket_cost("Glasgow", 1.6) == 104   

def test_plane_ticket_cost_first():
    assert plane_ticket_cost("New York", 1.9) == 3800
    assert plane_ticket_cost("Auckland", 1.9) == 1501
    assert plane_ticket_cost("Venice", 1.9) == 292.60
    assert plane_ticket_cost("Glasgow", 1.9) == 123.50 

def test_rental_car_cost_standard():
    assert rental_car_cost(2) == 60

def test_rental_car_cost_four_days():
    assert rental_car_cost(4) == 90

def test_rental_car_cost_seven_days():
    assert rental_car_cost(8) == 190

def test_total_cost():
    assert total_cost("New York", 8, 1.0) == 2680.00
    assert total_cost("Auckland", 4, 1.3) == 1327.00
    assert total_cost("Venice", 2, 1.6) == 376.40
    assert total_cost("Glasgow", 6, 1.9) == 623.50
