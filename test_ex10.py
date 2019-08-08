from ex10 import fizzbuzz

def test_fizzbuzz_number():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == "fizz"

def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == "buzz"

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"