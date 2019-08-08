from ex8 import deposit_calculator

def test_deposit_with_raise():
    assert deposit_calculator(1000000, 120000, 0.10, 0.02) == 132