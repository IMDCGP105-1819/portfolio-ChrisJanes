def deposit_calculator(total_cost, annual_salary, portion_saved, semi_annual_raise):
    r = 0.04
    portion_deposit = 0.20
    deposit_required = total_cost * portion_deposit
    current_savings = 0.0
    monthly_salary = annual_salary/12
    salary_savings = monthly_salary * portion_saved

    months = 0

    while current_savings < deposit_required:
        months = months + 1
        interest = (current_savings * r) / 12
        current_savings = current_savings + salary_savings + interest
        if months % 6 == 0:
            annual_salary = annual_salary + annual_salary * semi_annual_raise
            monthly_salary = annual_salary/12
            salary_savings = monthly_salary * portion_saved

    return months


print(deposit_calculator(1000000, 120000, 0.10, 0.02))