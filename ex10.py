def fizzbuzz(number):
    if number % 3 == 0:
        return "fizzbuzz" if number % 5 == 0 else "fizz"
    if number % 5 == 0:
        return "buzz"
    
    return number

for i in range(1,101):
    print(fizzbuzz(i))