
"""rent = 3500
month_not_rented = 1
running_cost = 600
COB = 750000
mortgage_cost = 0
years = 20"""


def ROI(rent, running_cost, COB, mortgage_cost, years, month_not_rented, agent, tax):
    expected_revenue = rent * (12-month_not_rented)
    project_cost = running_cost + COB + mortgage_cost + (COB*agent/100) + (COB*tax)
    net_profit = expected_revenue * years - (project_cost)
    ROI = net_profit / project_cost
    return ROI


def years_until_positive(result, rent, month_not_rented, running_cost, mortgage_cost, COB, appretiation, max_years, agent, tax, mortgage_years):
    yearly_breakdown = []
    yearly_running_cost = 12*running_cost
    yearly_mortgage_cost = 12*mortgage_cost
    while True:
        revenue = result * (rent * (12 - month_not_rented)) + COB * ((1+(appretiation/100))**result - 1)
        if result > mortgage_years:
            mortgage_cost = 0
        if result == 1:
            total_cost = (result * (yearly_running_cost + yearly_mortgage_cost)) + COB + (COB*(agent/100+tax))
        else:
            total_cost = total_cost + (12*running_cost + 12*mortgage_cost)
        yearly_breakdown.append({"year":result, "total cost": total_cost, "total revenue": revenue})
        result = result + 1
        if revenue > total_cost:
            return result, yearly_breakdown
        if result > max_years:
            return "Calculation exceeds maximum years limit", yearly_breakdown

#print(years_until_positive(rent, month_not_rented, running_cost, mortgage_cost, COB))

def price_EUR(price, fx):
    eur_price = price / fx
    return eur_price

def mortgage_payment(loan, interestrate, years):
    # number of payments
    n = years * 12
    monthly_rate = interestrate/1200
    if monthly_rate != 0:
        payment = (loan * monthly_rate * (1+monthly_rate)**n)/((1+monthly_rate)**n - 1)
        return payment
    else:
        return 0
    
def agent(agent, price):
    pln = (agent/100) * price
    return pln