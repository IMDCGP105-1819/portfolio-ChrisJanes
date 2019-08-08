def amount_to_save(annual_salary):
    semi_annual_raise = 0.07
    r = 0.04
    down_payment = 0.25
    total_cost = 1000000
    deposit_required = total_cost * down_payment

    max_guess = 10000

    epsilon = 100
    low = 0
    high = max_guess
    current_guess = (high + low) / 2
    steps = 0

    if annual_salary * 3 < deposit_required:
        return (False, 0.0, 0)

    current_savings = 0

    while abs(current_savings - deposit_required) > epsilon: 
        current_salary = annual_salary
        steps = steps + 1
        current_guess = (high + low) / 2
        portion_saved = current_guess / 100.0
        monthly_salary = current_salary/12
        salary_savings = monthly_salary * portion_saved
        months = 0
        current_savings = 0

        while months < 36:
            months = months + 1
            interest = (current_savings * r) / 12
            current_savings = current_savings + salary_savings + interest
            if months % 6 == 0:
                current_salary += current_salary * semi_annual_raise
                monthly_salary = current_salary/12
                salary_savings = monthly_salary * portion_saved

        print(current_savings, portion_saved, months)

        if current_savings < deposit_required:
            low = current_guess
            print("low")
        elif current_savings > deposit_required:
            high = current_guess
            print("high")
            
        if steps > 100:
            break

    return (True, round(current_guess / 100, 2), steps)

print(amount_to_save(100000))