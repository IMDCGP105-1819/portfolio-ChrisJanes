from car import Car

def test_car_init():
    car = Car("blue", "ford", "focus", 5)
    assert car.colour == "blue"
    assert car.manufacturer == "ford"
    assert car.model == "focus"
    assert car.doors == 5

def test_car_print(capsys):
    car = Car("blue", "ford", "focus", 5)
    print(car)
    captured = capsys.readouterr()
    assert captured.out == "Blue Ford Focus with 5 doors\n"