from ex9 import amount_to_save

def test_bisection_percentage():
    assert amount_to_save(100000) == (True, 0.66, 17)

def test_bisection_percentage_2():
    assert amount_to_save(10000) == (False, 0, 0)