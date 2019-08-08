from ex7 import deposit_calculator

def test_deposit():
    assert deposit_calculator(1000000, 120000, 0.10) == 154