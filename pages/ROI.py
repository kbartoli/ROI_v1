import streamlit as st
import pandas as pd
from helper import years_until_positive, ROI, mortgage_payment, price_EUR, agent

if not st.experimental_user.is_logged_in:
    st.write("Please log in to use the calculator!")
    st.stop()
    

# collecting info on the variables
st.title("Foundamental Project KPIs")
st.sidebar.title("Settings")
rent = st.sidebar.number_input("Monthly rent (PLN)", min_value= 1000, placeholder= "3000", step= 100)
month_not_rented = st.sidebar.number_input("Month / year not rented", min_value=0, max_value=12, step=1)
running_cost = st.sidebar.number_input("Monthly recurring cost (PLN)")
purchase_price = st.sidebar.number_input("Purchase price", min_value = 50000)
agent_comission = st.sidebar.slider("Agent comission (%)",min_value= 0.0, max_value= 10.0, step=0.1)
fx = st.sidebar.number_input("BCEE FX (1 Eur = x PLN)", min_value=3.0, step=0.01)
mortgage_amount = st.sidebar.number_input("Mortgage Amount (EUR)", min_value= 0, max_value=90000)
mortgage_rate = st.sidebar.slider("Mortgage rate (%)", min_value= 0.0, max_value= 10.0, step=0.05)
mortgage_years = st.sidebar.slider("Mortgage repayment periode (Years)", min_value=2, max_value=20)
years = st.sidebar.slider("ROI in years", min_value = 0, max_value= 40, step = 1)
appretiation = st.sidebar.slider("Appretiation rate (%)", min_value= 0.0, max_value= 10.0, step=0.05)
max_years = 50
calculate = st.sidebar.button("Calculate")
result = 1
tax = 0.02


# calculations
if calculate:
    eur_price = price_EUR(purchase_price, fx)
    st.write(f"**Purchase price:** EUR {eur_price}")
    monthly_mortgage_payment = mortgage_payment(mortgage_amount,mortgage_rate,mortgage_years)
    monthly_mortgage_payment_pln = monthly_mortgage_payment*fx
    st.write(f"**Monthly mortgage payment:** EUR {monthly_mortgage_payment}")
    return_on_investment = ROI(rent, running_cost, purchase_price, monthly_mortgage_payment, years, month_not_rented, agent_comission, tax)
    st.write(f"**Return on investment in {years} years:** {return_on_investment}%")
    
    investment_years, breakdown = years_until_positive(result= result, rent = rent, month_not_rented=month_not_rented, running_cost=running_cost, mortgage_cost=monthly_mortgage_payment_pln, COB = purchase_price, appretiation= appretiation, max_years=max_years, agent=agent_comission, tax=tax, mortgage_years=mortgage_years)
    st.write(f"Investment turns positive in **{investment_years}** years")
    total_tax_pln = purchase_price*tax
    total_tax_eur = price_EUR(total_tax_pln, fx)
    st.write(f"Tax: {total_tax_pln} in zloty and {total_tax_eur} in EUR")
    agent_cost_pln = agent(agent_comission, purchase_price)
    agent_cost_eur = price_EUR(agent_cost_pln, fx)
    st.write(f"Agent comission: ***{agent_cost_pln}*** in zloty and ***{agent_cost_eur}*** in EUR")

# putting things into a table
    kpis = {
        "Description":["**Purchase price in EUR**", "**Monthly mortgage payment**", "**Return on Investment**", "**Investment turns positive in**"],
        "Value":[eur_price,monthly_mortgage_payment, return_on_investment, investment_years]
    }

    df = pd.DataFrame(kpis)
    st.table(df)

    try:
        breakdown_df = pd.DataFrame(breakdown)
        st.write("*Yearly breakdown*")
        st.table(breakdown_df)
    except:
        st.write("Yearly breakdown not possible because calculation exceeds maximum year limit")
        st.write("Project will never turn positve")